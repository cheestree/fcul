import json
import time
from typing import Optional

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
    print("Total in table:", conn.execute(text("SELECT COUNT(*) FROM star_clusters")).fetchone()[0])


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


def queryMySQL(conn: Connection, filter: str):
    time_ip = time.time()
    result = conn.execute(text(f"SELECT * FROM star_clusters WHERE {filter}"))
    rows = result.fetchall()
    time_f = time.time()
    print('docs mysql = ', len(rows))
    print('total time mysql = ', time_f-time_ip)

#-------------------------------------------------------------------------------------------------#

def aggregateMongoDB(conn: Collection, pipeline: list):
    time_i = time.time()
    docs_nested = conn.aggregate(pipeline)
    docs_list = list(docs_nested)
    time_f = time.time()
    print('docs nested = ', len(docs_list))
    print('total time pymongo = ', time_f-time_i)
    return docs_list

def aggregateMySQL(conn: Connection, query: str):
    time_i = time.time()
    result = conn.execute(text(query))
    rows = result.fetchall()
    time_f = time.time()
    print('docs mysql = ', len(rows))
    print('total time mysql = ', time_f-time_i)
    return rows

#-------------------------------------------------------------------------------------------------#

def main():

    connMongoDB = createConnectionMongo("localhost", "27017", "root", "root", "openClusters", "cluster")
    connMySQL = createConnectionMySQL("localhost", "root", "root")

    loadMongoDB(connMongoDB)
    loadMySQL(connMySQL)

    queryMongoDB(connMongoDB, {"features.FeH": {"$lt": 0}, "features.Diam_pc": {"$gt": 10}})
    queryMySQL(connMySQL, "FeH < 0 AND Diam_pc > 10")

    mongoPipeline = [
        {
            "$match": {
                "features.FeH": {"$lt": 0, "$exists": True, "$ne": None},
                "features.Diam_pc": {"$gt": 10},
                "features.age": {"$exists": True, "$ne": None},
                "position.DE_ICRS": {"$exists": True, "$ne": None}
            }
        },
        {
            "$addFields": {
                "feh_bin": {
                    "$multiply": [
                        {"$floor": {"$divide": ["$features.FeH", 0.5]}},
                        0.5
                    ]
                }
            }
        },
        {
            "$group": {
                "_id": "$feh_bin",
                "avg_age": {"$avg": "$features.age"},
                "max_de_icrs": {"$max": "$position.DE_ICRS"},
                "cluster_count": {"$sum": 1}
            }
        },
        {
            "$sort": {"avg_age": -1}
        }
    ]
    print("MongoDB:")
    mongo_results = aggregateMongoDB(connMongoDB, mongoPipeline)
    for result in mongo_results:
        print(f"FeH bin: {result['_id']:.1f}, Avg Age: {result['avg_age']:.2f}, Max DE_ICRS: {result['max_de_icrs']:.4f}, Count: {result['cluster_count']}")

    mysqlQuery = """
    SELECT 
        FLOOR(FeH / 0.5) * 0.5 as feh_bin,
        AVG(age) as avg_age,
        MAX(DE_ICRS) as max_de_icrs,
        COUNT(*) as cluster_count
    FROM star_clusters 
    WHERE FeH < 0 AND Diam_pc > 10 
    AND FeH IS NOT NULL AND age IS NOT NULL AND DE_ICRS IS NOT NULL
    GROUP BY FLOOR(FeH / 0.5) * 0.5
    ORDER BY avg_age DESC
    """
    
    print("\nMySQL:")
    mysql_results = aggregateMySQL(connMySQL, mysqlQuery)
    for result in mysql_results:
        print(f"FeH bin: {result[0]:.1f}, Avg Age: {result[1]:.2f}, Max DE_ICRS: {result[2]:.4f}, Count: {result[3]}")

if __name__ == "__main__":
    main()

"""
Inserted documents: 1758
Total in collection: 1758
Total in table: 1758
docs nested =  275
total time pymongo =  7.581710815429688e-05
docs mysql =  275
total time mysql =  0.008218050003051758
MongoDB:
docs nested =  2
total time pymongo =  0.002195596694946289
FeH bin: -1.0, Avg Age: 8.28, Max DE_ICRS: -22.2106, Count: 1
FeH bin: -0.5, Avg Age: 8.10, Max DE_ICRS: 68.4630, Count: 274

MySQL:
docs mysql =  2
total time mysql =  0.0013885498046875
FeH bin: -1.0, Avg Age: 8.28, Max DE_ICRS: -22.2106, Count: 1
FeH bin: -0.5, Avg Age: 8.10, Max DE_ICRS: 68.4630, Count: 274
"""