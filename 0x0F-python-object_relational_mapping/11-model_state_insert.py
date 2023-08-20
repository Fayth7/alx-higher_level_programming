#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
Usage: ./11-model_state_insert.py <mysql username> /
                                  <mysql password> /
                                  <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)

    session.close()


if __name__ == "__main__":
    main()
