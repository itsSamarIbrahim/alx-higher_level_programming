#!/usr/bin/python3
"""
a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    session = Session(engine)
    new = State(name='Louisiana')
    session.add(new)

    new_state = session.query(State).filter(State.name == 'Louisiana').first()

    session.commit()
