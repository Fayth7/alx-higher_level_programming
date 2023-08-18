#!/usr/bin/python3
"""
Lists all States and corresponding Cities in the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(State, City).join(
        City).order_by(State.id, City.id)

    current_state = None
    for state, city in states_and_cities:
        if current_state is None or state != current_state:
            print("{}: {}".format(state.id, state.name))
            current_state = state
        print("    {}: {}".format(city.id, city.name))
