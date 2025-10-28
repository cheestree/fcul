import threading
import time
from configparser import Error

import mysql.connector
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text


def createAndLoadMySQL(host: str, user: str, password: str, database: str, port: int = 3306):
    df = pd.read_csv("../dias_catalogue.csv")
    df = df.replace('', None)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    engine_temp = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/")
    with engine_temp.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database}"))
        conn.commit()
    engine_temp.dispose()

    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")
        
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

#--------------------------------------------------------------#

def timedExecution(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

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

def createIndex(conn, index_name: str, table_name: str, column_name: str, spatial=False):
    create_index_query = f"CREATE INDEX {index_name} ON {table_name} ({column_name});"
    runQuery(conn, create_index_query)

def main():
    createAndLoadMySQL("localhost", "root", "root", "openclusters")
    conn = createConnection("localhost", "root", "root", "openclusters")

    # Needed due to max key length being exceeded. Text changed to maximum of 50 chars.
    runQuery(conn, "ALTER TABLE clusters MODIFY COLUMN Name VARCHAR(50);")

    query = "EXPLAIN SELECT * FROM clusters WHERE Name LIKE 'D%' AND RA_ICRS > 1 AND DE_ICRS < 25;"

    timedExecution(
        runQuery,
        conn,
        query,
        fetch=True
    )

    createIndex(conn, "comp_idx", "clusters", "Name,RA_ICRS,DE_ICRS")

    timedExecution(
        runQuery,
        conn,
        query,
        fetch=True
    )

if __name__ == "__main__":
    main()

"""
Connected to MySQL database 'openclusters'
Executed: ALTER TABLE clusters MODIFY COLUMN Name VARCHAR(50);
Rows returned: 1
(1, 'SIMPLE', 'clusters', 'ALL', None, None, None, None, '1758', 'Using where')
Executed: EXPLAIN SELECT * FROM clusters WHERE Name LIKE 'D%' AND RA_ICRS > 1 AND DE_ICRS < 25;
Execution time: 0.0011622905731201172 seconds
Executed: CREATE INDEX comp_idx ON clusters (Name,RA_ICRS,DE_ICRS);
Rows returned: 1
(1, 'SIMPLE', 'clusters', 'range', 'comp_idx', 'comp_idx', '212', None, '16', 'Using index condition')
Executed: EXPLAIN SELECT * FROM clusters WHERE Name LIKE 'D%' AND RA_ICRS > 1 AND DE_ICRS < 25;
Execution time: 0.0017921924591064453 seconds

The index is indeed being using as per 'Using index condition' in the second query, whilst the
first one is using a full table scan as indicated by 'Using where'.
"""