import argparse
from db import *

if __name__ == "__main__":
    conn = connectToDB()
    parser = argparse.ArgumentParser()

    parser.add_argument("query", help="Provide a complete SQL query to be executed")
    args = parser.parse_args()
    print(f"Executing: {args.query}")
    executeReadSQL(conn, args.query)
