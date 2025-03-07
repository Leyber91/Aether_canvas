# backend/db/model_mappers.py
from backend.models.graph import Graph
from backend.models.node import Node
from backend.models.edge import Edge
from backend.models.conversation import Conversation
from backend.models.message import Message
from backend.models.execution import Execution
from backend.models.execution_result import ExecutionResult

def map_to_domain(db_model):
    """Convert SQLAlchemy model instance to domain dictionary."""
    if db_model is None:
        return None
        
    # Extract model attributes into a dictionary
    result = {}
    for column in db_model.__table__.columns:
        result[column.name] = getattr(db_model, column.name)
    
    return result

def map_collection(models):
    """Convert a collection of models to dictionaries"""
    if models is None:
        return []
    return [map_to_domain(model) for model in models]

def map_to_db(model_class, data):
    """Convert dictionary to SQLAlchemy model instance."""
    instance = model_class()
    
    for key, value in data.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
    
    return instance