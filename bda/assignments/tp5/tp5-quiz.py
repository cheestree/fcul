import threading
import time

import mysql.connector


def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="openclusters"
    )


def unsafe_update(name, delay, col):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("START TRANSACTION")
    cur.execute(f"SELECT {col} FROM clusters WHERE name=%s FOR UPDATE", (name,))
    value = cur.fetchone()[0]
    print(f"[{threading.current_thread().name}] Read r50 = {value}")
    time.sleep(delay)
    new_value = value + 1
    cur.execute(f"UPDATE clusters SET {col}=%s WHERE name=%s", (new_value, name))
    conn.commit()
    print(f"[{threading.current_thread().name}] Updated r50 to {new_value}")

    cur.close()
    conn.close()

def get_value(col):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT {col} FROM clusters WHERE name='ASCC_105'")
    val = cur.fetchone()[0]
    cur.close(); conn.close()
    return val

def main():
    middleColumn = "DE_ICRS"

    initialValue = get_value(middleColumn)
    print(f"Initial {middleColumn} =", initialValue)
    # Two threads simulate two users updating the same record
    t1 = threading.Thread(target=unsafe_update, args=('ASCC_105', 2, middleColumn), name="UserA")
    t2 = threading.Thread(target=unsafe_update, args=('ASCC_105', 0, middleColumn), name="UserB")

    t1.start(); t2.start()
    t1.join(); t2.join()

    print(f"Final {middleColumn} =", get_value(middleColumn))

if __name__ == "__main__":
    main()

"""
Initial DE_ICRS = 27.3689
[UserA] Read r50 = 27.3689
[UserA] Updated r50 to 28.3689
[UserB] Read r50 = 28.3689
[UserB] Updated r50 to 29.3689
Final DE_ICRS = 29.3689
"""