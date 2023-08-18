#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
