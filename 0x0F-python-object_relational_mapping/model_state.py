#!/usr/bin/python3
"""Start link class to table in database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    DB_URL = 'mysql://username:password@localhost:3306/database_name'
    engine = create_engine(DB_URL)

    from model_state import State

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

