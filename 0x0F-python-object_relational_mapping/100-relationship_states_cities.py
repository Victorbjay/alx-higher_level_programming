#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco” in the database hbtn_0e_100_usa.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create new State object
    california = State(name='California')

    # Create new City object
    san_francisco = City(name='San Francisco', state=california)

    # Add the new State and City objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to the database
    session.commit()

