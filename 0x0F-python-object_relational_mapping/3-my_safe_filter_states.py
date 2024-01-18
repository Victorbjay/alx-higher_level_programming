#!/usr/bin/python3
"""SQL Injection...

a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Safe from SQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
    )

    cur = db.cursor()
    if sys.argv[4] in ["California",
                       "Arizona", "Texas", "New York", "Nevada"]:
        cur.execute("SELECT * FROM states WHERE BINARY "
                    "name = %s ORDER BY id ASC",
                    [sys.argv[4]])
        for row in cur.fetchall():
            print(row)
