from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from shared.config import config

DATABASE_URL = config.get_config('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=config.get_config('DEBUG_MODE'))
SessionLocal = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def get_session():
    return SessionLocal()
