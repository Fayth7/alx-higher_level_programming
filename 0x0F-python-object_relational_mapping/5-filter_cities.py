#!/usr/bin/python3
"""
Lists all cities of a specified state from the database hbtn_0e_4_usa.
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
        query = """
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        """
        cur.execute(query, (state_name,))
        row = cur.fetchone()
        if row:
            print(row[0])
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
