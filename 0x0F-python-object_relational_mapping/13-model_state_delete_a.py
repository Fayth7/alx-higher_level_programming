#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == '__main__':
    main()
