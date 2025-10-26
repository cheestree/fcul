
import time
from copy import Error

import mysql.connector
import numpy as np
import pandas as pd
import pymongo as pm
from pymongo import MongoClient
from sqlalchemy import create_engine, text


def createAndLoadMySQL(host: str, user: str, password: str):
    df = pd.read_csv("../dias_catalogue.csv")
    df = df.replace('', None)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    engine_temp = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/")
    with engine_temp.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS openclusters"))
        conn.commit()
    engine_temp.dispose()

    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/openclusters")
        
    df.insert(0, 'id', range(1, len(df) + 1))

    df.to_sql(name='clusters', con=engine, if_exists='replace', index=False)
    
    with engine.connect() as conn:
        conn.execute(text("ALTER TABLE clusters ADD PRIMARY KEY (id)"))
        conn.commit()

def createConnection(host: str, user: str, password: str, database: str, autocommit: bool = True):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            autocommit=autocommit
        )
        if mydb.is_connected():
            print(f"Connected to MySQL database '{database}'")
        return mydb
    except Error as e:
        print(f"Error: {e}")

def createConnectionMongo(host: str, port: str, user: str, password: str, cl: str, collection: str):
    client = pm.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin")
    mydb = client[cl]
    mycol = mydb[collection]
    return mycol

#--------------------------------------------------------------#

def runQuery(connection, query, fetch=False):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if fetch or query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            print(f"Rows returned: {len(rows)}")
            for row in rows:
                print(row)
        connection.commit()
        print(f"Executed: {query}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def runQueries(conn, queries):
    for query in queries:
        runQuery(conn, query)

def createIndex(conn, index_name: str, table_name: str, column_name: str, spatial=False):
    create_index_query = f"CREATE INDEX {index_name} ON {table_name} ({column_name});"
    runQuery(conn, create_index_query)

def createIndexes(conn, indexes: list, table_name: str):
    for index in indexes:
        index_name = index["name"]
        columns = index["columns"]
        # If columns is a list, join with commas
        if isinstance(columns, list):
            column_str = ", ".join(columns)
        else:
            column_str = str(columns)
        createIndex(conn, index_name, table_name, column_str)


def dropIndex(conn, index_name: str, table_name: str):
    drop_index_query = f"DROP INDEX {index_name} ON {table_name};"
    runQuery(conn, drop_index_query)

def dropIndexes(conn, index_names: list, table_name: str):
    for index_name in index_names:
        dropIndex(conn, index_name, table_name)

def explainQuery(connection, query):
    cursor = connection.cursor()
    cursor.execute("EXPLAIN " + query)
    rows = cursor.fetchall()
    print("\n🔎 EXPLAIN output:")
    for row in rows:
        print(row)
    cursor.close()

def showIndexes(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SHOW INDEXES FROM {table_name}")
    results = cursor.fetchall()
    print(f"\n Indexes for table '{table_name}':")
    for row in results:
        print(f"- {row[2]} on column {row[4]}")
    cursor.close()

def createClusterCoords(conn):
    df = pd.read_csv('../dias_catalogue.csv')

    # remove the whitespaces from the strings in "name" column
    df['name'] = df['name'].str.strip()

    # selects only the 'name','RA_ICRS', 'DE_ICRS', 'r50' columns 
    df =  df[[ 'name','RA_ICRS', 'DE_ICRS', 'r50']]
    new_df = df[['name', 'RA_ICRS', 'DE_ICRS']].copy()
    new_df_list = new_df.values.tolist()
    
    ### creates a new table 'cluster_coords'
    table_name = "cluster_coords"
    drop_table_query = f"DROP TABLE IF EXISTS {table_name};"
    runQuery(conn, drop_table_query)

    create_table_query = """
    CREATE TABLE cluster_coords (
        name VARCHAR(255),
        coords POINT NOT NULL
    );
    """

    # Execute the query to create the table

    runQuery(conn, create_table_query)

    insert_query = f"INSERT INTO cluster_coords (name, coords) VALUES (%s, POINT(%s, %s))"

    # Execute the query for each data record in the list
    mycursor = conn.cursor()
    mycursor.executemany(insert_query, new_df_list)
    conn.commit()

def explainClusterCoords(conn, cursor):
    sqlShowIndexes = "show index from cluster_coords"
    cursor.execute(sqlShowIndexes)
    indexList = cursor.fetchall()

    # Printing the list of indexes on the table cluster_coords
    print(indexList)

    # 2 create spacial index 
    create_index_query = f"CREATE SPATIAL INDEX coords_spatial_index ON cluster_coords (coords);"
    cursor.execute(create_index_query)
    conn.commit()

    # 3 show index list again

    sqlShowIndexes = "show index from cluster_coords"
    cursor.execute(sqlShowIndexes)
    indexList = cursor.fetchall()

    # Printing the list of indexes on the table cluster_coords

    print(indexList)

def createIndexMongo(col, fields, index_type: str = "asc"):
    # If fields is a string, make it a list
    if isinstance(fields, str):
        fields = [fields]
    # Build the index spec
    if index_type == "asc":
        index_spec = [(field, pm.ASCENDING) for field in fields]
    elif index_type == "desc":
        index_spec = [(field, pm.DESCENDING) for field in fields]
    elif index_type == "text":
        # Only one field can be text in a text index
        index_spec = [(fields[0], pm.TEXT)]
    elif index_type == "hashed":
        # Only one field can be hashed
        index_spec = [(fields[0], pm.HASHED)]
    else:
        print(f"Unknown index type: {index_type}")
        return
    col.create_index(index_spec)

def timedExecution(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")


def main():
    createAndLoadMySQL("localhost", "root", "root")
    conn = createConnection("localhost", "root", "root", "openclusters")
    cursor = conn.cursor()

    create_indexes = [
        {"name": "idx_coords", "columns": ["RA_ICRS", "DE_ICRS"]},
        {"name": "idx_distance", "columns": ["dist_iso"]},
        {"name": "idx_metallicity", "columns": ["FeH"]},
        {"name": "idx_age", "columns": ["age"]},
        {"name": "idx_name", "columns": ["name(50)"]}
    ]
    # Create indexes
    explain_query = """
        SELECT name, FeH, dist_iso
        FROM clusters
        WHERE FeH > -0.3 AND dist_iso < 1500;
    """
    createIndexes(conn, create_indexes, "clusters")

    # Show indexes
    showIndexes(conn, "clusters")

    # Explain query
    explainQuery(conn, explain_query)

    # Delete indexes
    drop_indexes = [
        "idx_coords",
        "idx_distance",
        "idx_metallicity",
        "idx_age",
        "idx_name"
    ]
    dropIndexes(conn, drop_indexes, "clusters")

    # Explain query
    explainQuery(conn, explain_query)

    # Cluster coords

    createClusterCoords(conn)
    explainClusterCoords(conn, cursor)

    # Part 2

    print("\n--- Part 2: Indexing in mySQL  ---\n")
    # Exercise 1
    print("\n--- Exercise 1: Query performance before and after indexing ---\n")

     # Query without indexes
    print("Query without indexes:")
    timedExecution(
        runQuery, conn, "EXPLAIN SELECT Plx, Name FROM clusters WHERE Plx > 10 AND dist_Plx < 5;", True
    )

    createIndexes(conn, [{"name": "plx_index", "columns": "Plx" }], "clusters")

    print("\n")
    print("Query with indexes:")
    timedExecution(
        runQuery, conn, "EXPLAIN SELECT Plx, Name FROM clusters WHERE Plx > 10 AND dist_Plx < 5;", True
    )

    # Drop the created index
    dropIndexes(conn, ["plx_index"], "clusters")

    # Exercise 2
    print("\n--- Exercise 2: Composite index performance ---\n")
    print("Query without composite index:")
    timedExecution(
        runQuery, conn, "EXPLAIN SELECT Plx, Name FROM clusters WHERE Plx > 10 AND dist_Plx < 5;", True
    )

    createIndex(conn, "plx_composite_index", "clusters", "Plx,dist_Plx")

    print("\n")
    print("Query with composite index:")
    timedExecution(
        runQuery, conn, "EXPLAIN SELECT Plx, Name FROM clusters WHERE Plx > 10 AND dist_Plx < 5;", True
    )    

    # Part 3

    print("\n--- Part 3: Indexing in MongoDB ---\n")

    # Exercise 1
    connMongoDB = createConnectionMongo("localhost", "27017", "root", "root", "openClusters", "cluster")

    print("\n--- Exercise 1: Query performance before and after indexing ---\n")
    print("Query without indexes:")
    timedExecution(
        connMongoDB.find,
        { "Plx": { "$gt": 10 } }
    )

    createIndexMongo(connMongoDB, "Plx", "asc")
    print("\n")
    print("Query with indexes:")
    timedExecution(
        connMongoDB.find,
        { "Plx": { "$gt": 10 }, "dist_Plx": { "$lt": 500 } }
    )

    # Exercise 2
    print("\n--- Exercise 2: Composite index performance ---\n")
    print("Query without composite index:")
    timedExecution(
        connMongoDB.find,
        { "Plx": { "$gt": 10 } }
    )

    createIndexMongo(connMongoDB, ["Plx", "dist_Plx"], "asc")
    print("\n")
    print("Query with composite index:")
    timedExecution(
        connMongoDB.find,
        { "Plx": { "$gt": 10 }, "dist_Plx": { "$lt": 500 } }
    )


if __name__ == "__main__":
    main()
