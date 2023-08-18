#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py <mysql username> /
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

    states_with_a = session.query(State).filter(
        State.name.like("%a%")).order_by(State.id)

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
