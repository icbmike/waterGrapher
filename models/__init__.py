import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.getenv(
    'DATABASE_URL', 'sqlite:///./test.db'), convert_unicode=True)

db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))
Base = declarative_base()
Base.query = db.query_property()

from models.user import User
from models.day import Day
from models.consumption import Consumption


def init_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    from sqlalchemy import MetaData
    m = MetaData(engine)
    m.reflect()
    m.drop_all()