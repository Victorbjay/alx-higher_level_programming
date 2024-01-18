#!/usr/bin/python3
"""Check for letter a.

Lists all State objects that contain the letter a from a database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    for object in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(object.id, object.name))
