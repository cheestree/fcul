import json
import time

import numpy as np
import pandas as pd
import pymongo as pm
from pymongo.database import Collection
from sqlalchemy import Connection, create_engine, text


def loadMongoDB(conn: Collection):
    df = pd.read_csv('../dias_catalogue.csv')

    # Create Nested dict (Object)
    df['position'] = df[['RA_ICRS', 'DE_ICRS', 'Plx', 'dist_PLX']].apply(
        lambda s: s.to_dict(), axis=1
    )
    df['features'] = df[['r50', 'Vr', 'age', 'FeH', 'Diam_pc']].apply(
        lambda s: s.to_dict(), axis=1
    )

    # Write out to a json file
    df[['name', 'position', 'features']].to_json("../dias_catalogue_filtered.json", 
    orient = "records", date_format = "epoch", 
    double_precision = 10, force_ascii = True, date_unit = "ms", 
    default_handler = None, indent=2)

    with open("../dias_catalogue_filtered.json", "r") as f:
        stars_data = json.load(f)

        # Step 3: Clear old data (optional, for repeat runs)
        conn.drop()

        # Step 4: Insert into MongoDB
        result = conn.insert_many(stars_data)

        print("Inserted documents:", len(result.inserted_ids))
        print("Total in collection:", conn.count_documents({}))

def loadMySQL(conn: Connection):
    # Load CSV
    df = pd.read_csv("../dias_catalogue.csv")

    # clean the dataset
    df = df.replace('', None)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    df.to_sql("star_clusters", conn, if_exists="replace", index=False)

def loadPandas():
    df = pd.read_csv('../dias_catalogue.csv')
    df['name'] = df['name'].str.strip()
    f =  df[[ 'name','RA_ICRS', 'DE_ICRS', 'Plx', 'dist_PLX', 'Vr', 'age', 'FeH', 'Diam_pc', 'r50']]
    return df


def createConnectionMySQL(host: str, user: str, password: str):
    engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/")
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS openclusters"))
        conn.commit()
    engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/openclusters")
    return engine.connect()

def createConnectionMongo(host: str, port: str, user: str, password: str, cl: str, collection: str):
    client = pm.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin")
    mydb = client[cl]
    mycol = mydb[collection]
    return mycol

#-------------------------------------------------------------------------------------------------#

from typing import Optional


def queryMongoDB(conn: Collection, filter: dict, sort: Optional[dict] = None, ascending: bool = True, limit: Optional[int] = None):
    time_i = time.time()
    docs_nested = conn.find(filter)
    if sort:
        sort_list = [(field, direction) for field, direction in sort.items()]
        docs_nested = docs_nested.sort(sort_list)
    if limit:
        docs_nested = docs_nested.limit(limit)
    
    time_f = time.time()
    docs_list = list(docs_nested)
    print('docs nested = ', len(docs_list))
    print('total time pymongo = ', time_f-time_i)

def aggregateMongoDB(conn: Collection):
    time_i = time.time()
    pipeline = [
        {
            "$group": {
                "_id": {
                    "$switch": {
                        "branches": [
                            { "case": { "$lt": ["$features.FeH", -1] }, "then": "FeH < -1" },
                            { "case": { "$and": [
                                { "$gte": ["$features.FeH", -1] },
                                { "$lte": ["$features.FeH", 0] }
                            ] }, "then": "-1 ≤ FeH ≤ 0" }
                        ],
                        "default": "FeH > 0"
                    }
                },
                "avg_Diam_pc": { "$avg": "$features.Diam_pc" },
                "max_Diam_pc": { "$max": "$features.Diam_pc" },
                "count": { "$sum": 1 }
            }
        },
        { "$sort": { "_id": 1 } }
    ]
    
    result = list(conn.aggregate(pipeline))
    time_f = time.time()
    
    print('MongoDB aggregation results:', len(result))
    print('total time MongoDB = ', time_f-time_i)
    for doc in result:
        print(f"Bin: {doc['_id']}, Avg: {doc['avg_Diam_pc']:.2f}, Max: {doc['max_Diam_pc']:.2f}, Count: {doc['count']}")

def aggregateMySQL(conn: Connection):
    time_i = time.time()
    result = conn.execute(text("""
        SELECT 
            CASE 
                WHEN FeH < -1 THEN 'FeH < -1'
                WHEN FeH >= -1 AND FeH <= 0 THEN '-1 ≤ FeH ≤ 0'
                WHEN FeH > 0 THEN 'FeH > 0'
                ELSE 'Unknown'
            END as FeH_bin,
            AVG(Diam_pc) as avg_Diam_pc,
            MAX(Diam_pc) as max_Diam_pc,
            COUNT(*) as count
        FROM star_clusters 
        WHERE FeH IS NOT NULL AND Diam_pc IS NOT NULL
        GROUP BY FeH_bin
        ORDER BY FeH_bin
    """))
    rows = result.fetchall()
    time_f = time.time()
    
    print('MySQL aggregation results:', len(rows))
    print('total time MySQL = ', time_f-time_i)
    for row in rows:
        print(f"Bin: {row[0]}, Avg: {row[1]:.2f}, Max: {row[2]:.2f}, Count: {row[3]}")

def aggregatePandas(df: pd.DataFrame):
    time_i = time.time()
    
    def create_feh_bins(feh):
        if pd.isna(feh):
            return "Unknown"
        elif feh < -1:
            return "FeH < -1"
        elif -1 <= feh <= 0:
            return "-1 ≤ FeH ≤ 0"
        else:
            return "FeH > 0"
    
    df_filtered = df[df['FeH'].notna() & df['Diam_pc'].notna()].copy()
    df_filtered['FeH_bin'] = df_filtered['FeH'].apply(create_feh_bins)
    result = df_filtered.groupby('FeH_bin')['Diam_pc'].agg(['mean', 'max', 'count']).reset_index()
    
    time_f = time.time()
    print('Pandas aggregation results:', len(result))
    print('total time Pandas = ', time_f-time_i)
    for _, row in result.iterrows():
        print(f"Bin: {row['FeH_bin']}, Avg: {row['mean']:.2f}, Max: {row['max']:.2f}, Count: {row['count']}")


def queryMySQL(conn: Connection, filter: str):
    time_ip = time.time()
    result = conn.execute(text(f"SELECT * FROM star_clusters WHERE {filter}"))
    rows = result.fetchall()
    time_f = time.time()
    print('docs mysql = ', len(rows))
    print('total time mysql = ', time_f-time_ip)

def queryPandas(df: pd.DataFrame, filter_condition):
    time_i = time.time()
    if isinstance(filter_condition, str):
        # For simple string conditions, use query()
        docs = df.query(filter_condition)
    else:
        # For complex conditions (lambda functions), call the function
        docs = filter_condition(df)
    time_fp = time.time()
    print('docs pandas = ', len(docs))
    print('total time Pandas = ', time_fp-time_i)

def main():

    connMongoDB = createConnectionMongo("localhost", "27017", "root", "root", "openClusters", "cluster")
    connMySQL = createConnectionMySQL("localhost", "root", "root")
    connPandas = loadPandas()

    loadMongoDB(connMongoDB)
    loadMySQL(connMySQL)

    #   Part 2
    print("Exercise 0: Basic Query - RA_ICRS > 50")
    queryMongoDB(connMongoDB, {'position.RA_ICRS': { "$gt": 50 }})
    queryMySQL(connMySQL, "RA_ICRS > 50")
    queryPandas(connPandas, "RA_ICRS > 50")

    #   Exercise 1
    print("Exercise 1: Complex Query - Name starts with 'A', RA_ICRS < 180, DE_ICRS between -60 and 60")
    queryMongoDB(connMongoDB, {
        'name': { "$regex": "^A" }, 
        'position.RA_ICRS': { "$lt": 180 }, 
        'position.DE_ICRS': { "$gt": -60, "$lt": 60 }
        })
    queryMySQL(connMySQL, "name LIKE 'A%' AND RA_ICRS < 180 AND DE_ICRS BETWEEN -60 AND 60")
    queryPandas(connPandas, lambda df: df[
        (df['name'].str.startswith('A', na=False)) & 
        (df['RA_ICRS'] < 180) & 
        (df['DE_ICRS'] > -60) & 
        (df['DE_ICRS'] < 60)
    ])

    #   Exercise 2
    print("Exercise 2: Combined Conditions - age > 4, FeH < 0, sorted by RA_ICRS ascending")
    queryMongoDB(connMongoDB, {
        'features.age': { "$gt": 4 },
        'features.FeH': { "$lt": 0 },
    }, sort={ 'position.RA_ICRS': 1 }, ascending=True)
    queryMySQL(connMySQL, "age > 4 AND FeH < 0 ORDER BY RA_ICRS ASC")
    queryPandas(connPandas, lambda df: df[
        (df['age'] > 4) & 
        (df['FeH'] < 0)
    ].sort_values(by='RA_ICRS', ascending=True))

    #   Exercise 3
    print("Exercise 3: Range Query - Diam_pc between 5 and 20, age < 9, limit 10 results")
    queryMongoDB(connMongoDB, {
        'features.Diam_pc': { "$gt": 5, "$lt": 20 },
        'features.age': { "$lt": 9 },
    }, limit=10)
    queryMySQL(connMySQL, "Diam_pc BETWEEN 5 AND 20 AND age < 9 LIMIT 10")
    queryPandas(connPandas, lambda df: df[
        (df['Diam_pc'] > 5) & 
        (df['Diam_pc'] < 20) & 
        (df['age'] < 9)
    ].head(10))

    #   Exercise 4
    print("Exercise 4: OR Conditions - (RA_ICRS between 100 and 200 and DE_ICRS > 0) or (RA_ICRS < 50 and DE_ICRS < -30)")
    queryMongoDB(connMongoDB, {
        '$or': [
        { 'position.RA_ICRS': { "$gt": 100, "$lt": 200 }, 'position.DE_ICRS': { "$gt": 0 } },
        { 'position.RA_ICRS': { "$lt": 50 }, 'position.DE_ICRS': { "$lt": -30 } }
        ]
    })
    queryMySQL(connMySQL, "(RA_ICRS BETWEEN 100 AND 200 AND DE_ICRS > 0) OR (RA_ICRS < 50 AND DE_ICRS < -30)")
    queryPandas(connPandas, lambda df: df[
        ((df['RA_ICRS'] > 100) & (df['RA_ICRS'] < 200) & (df['DE_ICRS'] > 0)) |
        ((df['RA_ICRS'] < 50) & (df['DE_ICRS'] < -30))
    ])

    #   Exercise 5
    print("Exercise 5: Aggregation - Average and Max Diam_pc by FeH bins")
    aggregateMongoDB(connMongoDB)
    aggregateMySQL(connMySQL)
    aggregatePandas(connPandas)



if __name__ == "__main__":
    main()