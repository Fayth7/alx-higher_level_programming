#!/usr/bin/python3

import sys
import MySQLdb

if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

username, password, database = sys.argv[1:4]

try:
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
except MySQLdb.Error as e:
    print("MySQL Error:", e)
finally:
    cur.close()
    db.close()
