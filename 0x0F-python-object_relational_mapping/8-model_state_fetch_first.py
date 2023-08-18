#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
Usage: ./8-model_state_fetch_first.py <mysql username> /
                                     <mysql password> /
                                     <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    
    print(f"{first_state.id}: {first_state.name}" if first_state else "Nothing")

    session.close()

if __name__ == "__main__":
    main()
