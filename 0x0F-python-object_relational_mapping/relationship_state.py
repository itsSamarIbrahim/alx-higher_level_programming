#!/usr/bin/python3
"""a python file that contains the class definition of a State and
an instance Base = declarative_base()"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """creating a class State"""

    __tablename__ = 'states'

    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False,
        unique=True)

    name = Column(String(128), nullable=False)

    cities = relationship(
        'City',
        backref='state',
        cascade='all, delete-orphan')
