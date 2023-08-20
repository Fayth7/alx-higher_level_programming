#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base


def create_california_with_san_francisco(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    session.add(california)
    session.add(san_francisco)
    session.commit()


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    create_california_with_san_francisco(engine)
