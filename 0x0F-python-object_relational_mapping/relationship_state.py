#!/usr/bin/python3
"""
Module that contains the class definition of a State.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City

class State(Base):
    """
    Class that represents the State table.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

