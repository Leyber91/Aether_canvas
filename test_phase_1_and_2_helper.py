from backend.db.sqlalchemy_manager import Base, engine
from backend.models.graph import Graph
from backend.models.execution import Execution
from backend.models.execution_result import ExecutionResult
from backend.models.node import Node
from backend.models.edge import Edge

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
