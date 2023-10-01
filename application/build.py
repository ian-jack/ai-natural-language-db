import os
from db import *
from schema import *
from data import *

if __name__ == "__main__":
    conn = connectToDB()

    print("Creating cow")
    executeWriteSQL(conn, create_cow_table)
    print("Loading cow")
    executeWriteSQL(conn, load_cow_table)
    print("Creating milk_yield")
    executeWriteSQL(conn, create_milk_yield_table)
    print("Loading milk_yield")
    executeWriteSQL(conn, load_milk_yield_table)

    print("Done did a good build")
