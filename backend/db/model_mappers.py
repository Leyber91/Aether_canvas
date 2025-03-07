from backend.models.graph import Graph
from backend.models.node import Node
from backend.models.edge import Edge
from backend.models.conversation import Conversation
from backend.models.message import Message
from backend.models.execution import Execution
from backend.models.execution_result import ExecutionResult

def map_to_domain(db_model):
    """Convert SQLAlchemy model instance to domain dictionary."""
    if isinstance(db_model, Graph):
        return {
            'id': db_model.id,
            'name': db_model.name,
            'description': db_model.description,
            'graph_metadata': db_model.graph_metadata
        }
    elif isinstance(db_model, Node):
        return {
            'id': db_model.id,
            'graph_id': db_model.graph_id,
            'name': db_model.name,
            'node_metadata': db_model.node_metadata
        }
    elif isinstance(db_model, Edge):
        return {
            'id': db_model.id,
            'source_id': db_model.source_id,
            'target_id': db_model.target_id,
            'edge_metadata': db_model.edge_metadata
        }
    elif isinstance(db_model, Conversation):
        return {
            'id': db_model.id,
            'node_id': db_model.node_id,
            'title': db_model.title,
            'conversation_metadata': db_model.conversation_metadata
        }
    elif isinstance(db_model, Message):
        return {
            'id': db_model.id,
            'conversation_id': db_model.conversation_id,
            'role': db_model.role,
            'content': db_model.content,
            'message_metadata': db_model.message_metadata
        }
    elif isinstance(db_model, Execution):
        return {
            'id': db_model.id,
            'graph_id': db_model.graph_id,
            'status': db_model.status,
            'execution_metadata': db_model.execution_metadata
        }
    elif isinstance(db_model, ExecutionResult):
        return {
            'id': db_model.id,
            'execution_id': db_model.execution_id,
            'node_id': db_model.node_id,
            'result': db_model.result,
            'error': db_model.error,
            'execution_time_ms': db_model.execution_time_ms
        }
    else:
        raise TypeError(f"Unhandled type: {type(db_model)}")

def map_to_db(model_class, data):
    """Convert dictionary to SQLAlchemy model instance."""
    return model_class(**data)
