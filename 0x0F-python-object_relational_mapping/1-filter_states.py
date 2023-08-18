#!/usr/bin/python3
"""
Lists states with a name starting with 'N' from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
