#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py <mysql username> /
                                         <mysql password> /<database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


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

    city_state_pairs = session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id).all()

    for city, state in city_state_pairs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
