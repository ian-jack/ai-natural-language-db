import sqlite3
from sqlite3 import Error

db_string = "./dairy.db"

def connectToDB():
    try:
        print("Connecting")
        return sqlite3.connect(db_string)
    except Error:
        print(Error)

def executeWriteSQL(conn, query):
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except Error as e:
        print(e)

def executeReadSQL(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)
