#!/usr/bin/python3
"""
Lists the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Usage: ./10-model_state_my_get.py <mysql username> /
                                  <mysql password> /
                                  <database name>
                                  <state name searched>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password>"
              " <database> <state name searched>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
