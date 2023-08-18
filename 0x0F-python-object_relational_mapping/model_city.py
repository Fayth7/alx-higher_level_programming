#!/usr/bin/python3
"""
Defines a City model.
Inherits from SQLAlchemy Base and links to the MySQL table cities.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city for a MySQL database.
    Attributes:
        id (int): The city's id.
        name (str): The city's name.
        state_id (int): The city's state id.
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


def main():
    pass  # Add code to create, query, or modify City objects here


if __name__ == "__main__":
    main()
