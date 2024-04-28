#!/usr/bin/python3
"""
a script prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base
    from model_state import State
    from model_city import City
    import sys

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    for state, city in session.query(State, City).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
