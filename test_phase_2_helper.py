# Drop existing tables and recreate them (ONLY for dev/test)
from backend.db.sqlalchemy_manager import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
