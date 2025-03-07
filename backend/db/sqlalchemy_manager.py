# backend/db/sqlalchemy_manager.py
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

# Add this class to make the test code work without changing it
class SQLAlchemyManager:
    """Class wrapper for the existing SQLAlchemy functions"""
    
    @classmethod
    def init_db(cls):
        """Initialize the database schema"""
        init_db()
    
    @classmethod
    def get_session(cls):
        """Get a database session"""
        return get_session()
    
    @classmethod
    def get_base(cls):
        """Get the SQLAlchemy Base class"""
        return Base