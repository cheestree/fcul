import mysql.connector
from mysql.connector.cursor import MySQLCursorAbstract
import numpy as np
import pandas as pd

def readCSV(file_name: str):
    try:
        csv = pd.read_csv(file_name)
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    return csv

def map_dtype_to_mysql(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INT"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    else:
        return "VARCHAR(255)"

def createColumns(csv: pd.DataFrame):
    columns = ['id INT AUTO_INCREMENT PRIMARY KEY']
    for col, dtype in csv.dtypes.items():
        sql_type = map_dtype_to_mysql(dtype)
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

def createTable(cursor: MySQLCursorAbstract, table: str, columns: str):
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    cursor.execute(f"CREATE TABLE {table} ({columns})")

def insertRow(cursor: MySQLCursorAbstract, table: str, df: pd.DataFrame):
    cols = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    values = tuple(x.item() if hasattr(x, "item") else x for x in df.iloc[0])
    cursor.execute(sql, values)

def insertMultipleRows(cursor: MySQLCursorAbstract, table: str, csv: pd.DataFrame):
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

def selectRows(cursor: MySQLCursorAbstract, table: str, column: str, threshold: int):
    sql = f"SELECT * FROM {table} WHERE {column} > %s"
    cursor.execute(sql, (threshold,))
    for row in cursor.fetchall():
        print(row)

def selectSpecificColumns(cursor: MySQLCursorAbstract):
    cursor.execute("SELECT name, RA_ICRS, DE_ICRS, Diam_pc FROM star_clusters WHERE Plx > %s", (1,))
    for row in cursor.fetchall():
        print(row)

def updateAgeOfSpecificRowBasedOnName(cursor: MySQLCursorAbstract, name: str, age: int):
    cursor.execute("UPDATE star_clusters SET age = %s WHERE name = %s", (age, name,))
    count = cursor.rowcount
    print(count)

def deleteRow(cursor: MySQLCursorAbstract, name: str):
    cursor.execute("DELETE FROM star_clusters WHERE name = %s", (name,))
    count = cursor.rowcount
    print(count)

def findByName(cursor: MySQLCursorAbstract, name: str):
    cursor.execute("SELECT name, dist_PLX FROM star_clusters WHERE name LIKE %s", (f"%{name}%",))
    for row in cursor.fetchall():
        print(row)

def aggregateFunction(cursor: MySQLCursorAbstract):
    cursor.execute("SELECT count(*) FROM star_clusters WHERE FeH < 0")
    result = cursor.fetchone()
    print(result[0])


#   NaN values are replaced with None to be compatible with MySQL.
#   
#   Inf and -inf, however, are replaced with None to represent infinites in MySQL.
#   Given that the choices could be zero, -1 and null, it was decided to use None.
#   Zero would represent a 0 distance value, -1 is also a valid distance and null can
#   be treated as a too big of a number distance.
#   
#   None, as a value, is represented by Null in the database, since NaN isn't supported.
def main():
    csv = readCSV("dias_catalogue.csv")
    csv = csv.replace('', None)
    csv = csv.replace([np.nan, np.inf, -np.inf], None)

    #   Exercise 1
    connection = createConnection("localhost", "root", "root")
    cursor = connection.cursor()

    createDatabase(cursor, "astronomy_db")
    
    #   Exercise 2
    columns = createColumns(csv)
    createTable(cursor, "star_clusters", columns)

    #   Exercise 3
    insertRow(cursor, "star_clusters", csv.head(1))

    #   Exercise 4
    #   insertMultipleRows(cursor, "star_clusters", "dias_catalogue.csv")
    insertMultipleRows(cursor, "star_clusters", csv)
    connection.commit()

    #   Exercise 5
    selectRows(cursor, "star_clusters", "DiamMax_pc", 20)

    #   Exercise 6
    selectSpecificColumns(cursor)

    #   Exercise 7
    updateAgeOfSpecificRowBasedOnName(cursor, "NGC 188", 999)
    connection.commit()

    #   Exercise 8
    deleteRow(cursor, "NGC 188")
    connection.commit()

    #   Exercise 9
    findByName(cursor, "NGC")

    #   Exercise 10
    aggregateFunction(cursor)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()