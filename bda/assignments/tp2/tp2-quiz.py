import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text


def clusterSizeAndExtent(conn):
    query = text("""SELECT name, Diam_pc, dist_iso FROM star_clusters ORDER BY Diam_pc DESC LIMIT 5;""")
    results = conn.execute(query).fetchall()
    for row in results:
        print(row)

def motionAnalysis(conn):
    query = text("""SELECT avg(pmRA), avg(pmDE) FROM star_clusters WHERE Plx > 1;""")
    results = conn.execute(query).fetchall()
    for row in results:
        print(row)

def distanceCmparison(conn):
    query = text("""SELECT * FROM star_clusters WHERE dist_iso - dist_PLX > 500;""")
    results = conn.execute(query).fetchall()
    for row in results:
        print(row)

def ageAndMetallicity(conn):
    query = text("""SELECT avg(FeH) FROM star_clusters WHERE age > 2;""")
    results = conn.execute(query).fetchall()
    for row in results:
        print(row)

def filteringByDataQuality(conn):
    query = text("""SELECT name, Plx, sigPM, e_Plx FROM star_clusters WHERE sigPM < 0.5 AND e_Plx < 0.2;""")
    results = conn.execute(query).fetchall()
    for row in results:
        print(row)

def query_cluster_by_name(conn, cluster_name: str):
    query = text("""SELECT * FROM star_clusters WHERE name = :name;""")
    result = pd.read_sql_query(query, conn, params={"name": cluster_name})
    print(result)

def main():
    # Load CSV
    df = pd.read_csv("dias_catalogue.csv")

    # clean the dataset
    df = df.replace('', None)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Create a connection to MySQL
    # Replace user, password, host, port, database_name with your info
    #engine = create_engine("mysql+mysqlconnector://user:password@host:port/database_name")
    engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/")
    # Execute raw SQL to create database
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS astro_database"))
        conn.commit()
    engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/astro_database")

    df.to_sql("star_clusters", engine, if_exists="replace", index=False)

    with engine.connect() as conn:
        #   Exercise 1
        print("Exercise 1")
        clusterSizeAndExtent(conn)

        #   Exercise 2
        print("Exercise 2")
        motionAnalysis(conn)

        #   Exercise 3
        print("Exercise 3")
        distanceCmparison(conn)

        #   Exercise 4
        print("Exercise 4")
        ageAndMetallicity(conn)

        #   Exercise 5
        print("Exercise 5")
        filteringByDataQuality(conn)

        #   Exercise 6
        print("Exercise 6")
        query_cluster_by_name(conn, "ASCC_99")

if __name__ == "__main__":
    main()