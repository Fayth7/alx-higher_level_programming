#!/usr/bin/python3
"""
Displays values in states table hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        cur.execute(query, (state_name,))
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
