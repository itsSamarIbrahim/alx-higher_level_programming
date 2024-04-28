#!/usr/bin/python3
"""
the class definition of a City
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    """creating a class City"""

    __tablename__ = 'cities'

    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False,
        unique=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
