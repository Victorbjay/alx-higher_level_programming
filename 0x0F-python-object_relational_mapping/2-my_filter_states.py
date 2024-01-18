#!/usr/bin/python3
"""Filter states by user input.

A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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
    q = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(
        sys.argv[4])
    cur.execute(q)
    for row in cur.fetchall():
        print(row)
