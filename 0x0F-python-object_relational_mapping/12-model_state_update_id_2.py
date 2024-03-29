#!/usr/bin/python3
"""
a script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base
    from model_state import State
    import sys

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()

    session.close()
