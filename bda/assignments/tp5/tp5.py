import mysql.connector
import numpy as np
import pandas as pd
from mysql.connector.cursor import MySQLCursorAbstract
from sqlalchemy import Connection, create_engine, text


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
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        autocommit=autocommit
    )
    return mydb

def basicTransaction():
    # Session A
    connA = createConnection("localhost", "root", "root", "openclusters")
    cursorA = connA.cursor()
    
    # Session B
    connB = createConnection("localhost", "root", "root", "openclusters")
    cursorB = connB.cursor()
    
    try:
        cursorA.execute("START TRANSACTION")
        cursorA.execute("UPDATE clusters SET r50 = r50 + 5 WHERE id = 1")
        print("Session A: Updated r50, not committed yet.")
        
        # Session B
        cursorB.execute("SELECT r50 FROM clusters WHERE id = 1")
        result = cursorB.fetchone()
        print(f"Session B reads: {result[0]}")
        
        connA.commit()
        print("Session A: Committed")
    finally:
        cursorA.close()
        cursorB.close()
        connA.close()
        connB.close()

def dirtyReadTransaction():
    connA = createConnection("localhost", "root", "root", "openclusters")
    cursorA = connA.cursor()
    
    connB = createConnection("localhost", "root", "root", "openclusters")
    cursorB = connB.cursor()
    
    try:
        cursorA.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED")
        cursorB.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED")
        
        cursorA.execute("START TRANSACTION")
        cursorA.execute("UPDATE clusters SET Vr = Vr + 10 WHERE id = 2")
        print("Session A: Updated Vr, not committed yet.")
        
        # Session B
        cursorB.execute("START TRANSACTION")
        cursorB.execute("SELECT Vr FROM clusters WHERE id = 2")
        result = cursorB.fetchone()
        print(f"Session B reads (dirty read): {result[0]}")
        
        connA.rollback()  # Session A
        print("Session A: Rolled back")
    finally:
        cursorA.close()
        cursorB.close()
        connA.close()
        connB.close()

def nonRepeatableReadTransaction():
    connA = createConnection("localhost", "root", "root", "openclusters")
    cursorA = connA.cursor()
    
    connB = createConnection("localhost", "root", "root", "openclusters")
    cursorB = connB.cursor()
    
    try:
        cursorA.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
        
        cursorA.execute("START TRANSACTION")
        cursorA.execute("SELECT FeH FROM clusters WHERE id = 3")
        result1 = cursorA.fetchone()
        print(f"Session A first read: {result1[0]}")
        
        # Session B updates and commits
        cursorB.execute("UPDATE clusters SET FeH = FeH + 0.1 WHERE id = 3")
        connB.commit()
        print("Session B: Updated and committed")
        
        # Session A reads again
        cursorA.execute("SELECT FeH FROM clusters WHERE id = 3")
        result2 = cursorA.fetchone()
        print(f"Session A second read: {result2[0]}")
        
        connA.commit()
    finally:
        cursorA.close()
        cursorB.close()
        connA.close()
        connB.close()

def phantomReadTransaction():
    connA = createConnection("localhost", "root", "root", "openclusters")
    cursorA = connA.cursor()
    
    connB = createConnection("localhost", "root", "root", "openclusters")
    cursorB = connB.cursor()
    
    try:
        cursorA.execute("SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ")
        
        cursorA.execute("START TRANSACTION")
        cursorA.execute("SELECT COUNT(*) FROM clusters WHERE Diam_pc > 10")
        count1 = cursorA.fetchone()[0]
        print(f"Session A first count: {count1}")
        
        # Session B
        cursorB.execute("""
            INSERT INTO clusters (id, name, r50, Vr, age, FeH, Diam_pc) 
            VALUES (9999, 'NewCluster', 5.0, 0.0, 2.5, -0.1, 12.0)
        """)
        connB.commit()
        print("Session B: Inserted new row and committed")
        
        # Session A
        cursorA.execute("SELECT COUNT(*) FROM clusters WHERE Diam_pc > 10")
        count2 = cursorA.fetchone()[0]
        print(f"Session A second count: {count2}")
        
        connA.commit()
    finally:
        cursorA.close()
        cursorB.close()
        connA.close()
        connB.close()

def serializableTransaction():
    connA = createConnection("localhost", "root", "root", "openclusters", autocommit=False)
    cursorA = connA.cursor()
    
    connB = createConnection("localhost", "root", "root", "openclusters", autocommit=False)
    cursorB = connB.cursor()
    
    try:
        cursorA.execute("SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE")
        
        cursorA.execute("START TRANSACTION")
        cursorA.execute("SELECT * FROM clusters WHERE FeH < 0")
        results = cursorA.fetchall()
        print(f"Session A: Selected {len(results)} rows with FeH < 0")
        
        # Session B
        try:
            cursorB.execute("""
                INSERT INTO clusters (id, name, r50, Vr, age, FeH, Diam_pc) 
                VALUES (9998, 'TempCluster', 4.0, 0.0, 1.2, -0.3, 7.5)
            """)
            connB.commit()
            print("Session B: Insert succeeded")
        except mysql.connector.errors.DatabaseError as e:
            print(f"Session B: Insert blocked/failed - {e}")
        
        connA.commit()
    finally:
        cursorA.close()
        cursorB.close()
        connA.close()
        connB.close()

def main():
    createAndLoadMySQL("localhost", "root", "root")

    #   Exercise 1: No, it does not, as the default isolation level is REPEATABLE READ,
    #   which prevents dirty reads, a read operation from seeing uncommitted changes
    #   from other transactions.
    basicTransaction()

    #   Exercise 2: Yes, it does, as we specify the isolation level to READ UNCOMMITTED.
    #   This allows dirty reads, meaning a read operation can see uncommitted changes
    #   from other transactions.
    dirtyReadTransaction()

    #   Exercise 3: Yes, it does, as we specify the isolation level to READ COMMITTED.
    #   This allows non-repeatable reads, meaning a read operation can see changes
    #   committed by other transactions after the initial read.
    nonRepeatableReadTransaction()

    #   Exercise 4: No, it did NOT prevent phantom reads in THEORY, but MySQL's 
    #   implementation of REPEATABLE READ actually DOES prevent phantom reads using
    #   Next-Key Locking. This is different from the SQL standard, where REPEATABLE READ
    #   allows phantom reads. In this case, Session A will see the SAME count both times
    #   because MySQL locks the range, preventing Session B's insert from being visible
    #   to Session A's transaction.
    phantomReadTransaction()

    #   Exercise 5: It is blocked, as we specify the isolation level to SERIALIZABLE.
    #   Serializable prevents phantom reads by ensuring that transactions are executed
    #   in a way that they appear to be serialized, thus preventing other transactions
    #   from inserting new rows that would affect the result set of the initial read.
    serializableTransaction()


if __name__ == "__main__":
    main()


