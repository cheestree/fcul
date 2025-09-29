import mysql.connector
import numpy as np
import pandas as pd
from mysql.connector.cursor import MySQLCursorAbstract


def readCSV(file_name: str):
    try:
        csv = pd.read_csv(file_name)
    except Exception as e:
        raise Exception(f"Error loading file {e}")
    return csv

def mapDtypeToMysql(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INT"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    else:
        return "VARCHAR(32)"

def createColumns(csv: pd.DataFrame):
    columns = ['id INT AUTO_INCREMENT PRIMARY KEY']
    for col, dtype in csv.dtypes.items():
        sql_type = mapDtypeToMysql(dtype)
        columns.append(f"`{col}` {sql_type}")
    return ", ".join(columns)



def createConnection(host: str, user: str, password: str):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        allow_local_infile=True
    )
    return mydb

def createDatabase(cursor: MySQLCursorAbstract, database: str):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    cursor.execute(f"USE {database}")

def createTable(cursor: MySQLCursorAbstract, columns: str, table: str = "star_clusters"):
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    cursor.execute(f"CREATE TABLE {table} ({columns})")

def insertRow(cursor: MySQLCursorAbstract, df: pd.DataFrame, table: str = "star_clusters"):
    cols = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    values = tuple(x.item() if hasattr(x, "item") else x for x in df.iloc[0])
    cursor.execute(sql, values)

def insertMultipleRows(cursor: MySQLCursorAbstract, csv: pd.DataFrame, table: str = "star_clusters"):
    cols = ", ".join([f"`{col}`" for col in csv.columns])
    placeholders = ", ".join(["%s"] * len(csv.columns))
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    values = list(csv.itertuples(index=False, name=None))

    cursor.executemany(sql, values)
    print(cursor.rowcount)

'''
def insertMultipleRows(cursor: MySQLCursorAbstract, table: str, file: str):
    sql = f''LOAD DATA LOCAL INFILE '{file}'
            INTO TABLE {table}
            FIELDS TERMINATED BY ','
            ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 LINES;
        ''
    cursor.execute(sql)
'''

def selectRows(cursor: MySQLCursorAbstract, column: str, threshold: int, table: str = "star_clusters"):
    sql = f"SELECT * FROM {table} WHERE {column} > %s"
    cursor.execute(sql, (threshold,))
    for row in cursor.fetchall():
        pass
        #   print(row)
    print(len(cursor.fetchall()))

def selectSpecificColumns(cursor: MySQLCursorAbstract, table: str = "star_clusters", columns: list[str] = ['name', 'RA_ICRS', 'DE_ICRS', 'Diam_pc']):
    cursor.execute(f"SELECT {", ".join(columns)} FROM {table} WHERE Plx > %s", (1,))
    for row in cursor.fetchall():
        pass
        #   print(row)
    print(len(cursor.fetchall()))

def updateAgeOfSpecificRowBasedOnName(cursor: MySQLCursorAbstract, name: str, age: int, table: str = "star_clusters"):
    cursor.execute(f"UPDATE {table} SET age = %s WHERE name = %s", (age, name,))
    print(cursor.rowcount)

def deleteRow(cursor: MySQLCursorAbstract, name: str, table: str = "star_clusters"):
    cursor.execute(f"DELETE FROM {table} WHERE name = %s", (name,))
    print(cursor.rowcount)

def findByName(cursor: MySQLCursorAbstract, name: str, columns: list[str] = ['name', 'dist_PLX'], table: str = "star_clusters"):
    cursor.execute(f"SELECT {", ".join(columns)} FROM {table} WHERE name LIKE %s", (f"%{name}%",))
    for row in cursor.fetchall():
        pass
        #   print(row)
    print(len(cursor.fetchall()))

def aggregateFunction(cursor: MySQLCursorAbstract, table: str = "star_clusters"):
    cursor.execute(f"SELECT count(*) FROM {table} WHERE FeH < 0")
    print(cursor.fetchone()[0])


#   NaN values are replaced with None to be compatible with MySQL.
#   
#   Inf and -inf, however, are replaced with None to represent infinites in MySQL.
#   Given that the choices could be zero, -1 and null, it was decided to use None.
#   Zero would represent a 0 distance value, -1 is also a valid distance and null can
#   be treated as a too big of a number distance.
#   
#   None, as a value, is represented by Null in the database, since NaN isn't supported.
def main():
    csv = readCSV("../dias_catalogue.csv")
    csv = csv.replace('', None)
    csv = csv.replace([np.nan, np.inf, -np.inf], None)

    #   Exercise 1
    print("Exercise 1")
    with createConnection("localhost", "root", "root") as connection:
        with connection.cursor() as cursor:
            createDatabase(cursor, "astronomy_db")
            
            #   Exercise 2
            print("Exercise 2")
            columns = createColumns(csv)
            createTable(cursor, columns)

            #   Exercise 3
            print("Exercise 3")
            insertRow(cursor, csv.head(1))

            #   Exercise 4
            print("Exercise 4")
            #   insertMultipleRows(cursor, "star_clusters", "dias_catalogue.csv")
            insertMultipleRows(cursor, csv)
            connection.commit()

            #   Exercise 5
            print("Exercise 5")
            selectRows(cursor, "DiamMax_pc", 20)

            #   Exercise 6
            print("Exercise 6")
            selectSpecificColumns(cursor)

            #   Exercise 7
            print("Exercise 7")
            updateAgeOfSpecificRowBasedOnName(cursor, "NGC_188", 999)
            connection.commit()

            #   Exercise 8
            print("Exercise 8")
            deleteRow(cursor, "NGC_188")
            connection.commit()

            #   Exercise 9
            print("Exercise 9")
            findByName(cursor, "NGC")

            #   Exercise 10
            print("Exercise 10")
            aggregateFunction(cursor)

if __name__ == "__main__":
    main()