# backend/repositories/execution_repository.py
from sqlalchemy.orm import joinedload
from backend.db.sqlalchemy_manager import SQLAlchemyManager
from backend.models.execution import Execution
from backend.models.execution_result import ExecutionResult
from backend.db.model_mappers import map_to_domain, map_collection
from datetime import datetime
import uuid

class ExecutionRepository:
    def __init__(self):
        self.db_manager = SQLAlchemyManager()
    
    def create(self, execution_data):
        """Create a new execution record"""
        session = self.db_manager.get_session()
        try:
            execution = Execution(
                id=execution_data["id"],
                graph_id=execution_data["graph_id"],
                status=execution_data["status"],
                execution_metadata=execution_data["execution_metadata"],
                started_at=execution_data["started_at"],
                completed_at=execution_data["completed_at"]
            )
            session.add(execution)
            session.commit()
            return map_to_domain(execution)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def find_by_id(self, execution_id):
        """Find an execution by ID"""
        session = self.db_manager.get_session()
        try:
            execution = session.query(Execution).get(execution_id)
            return map_to_domain(execution) if execution else None
        finally:
            session.close()
    
    def find_by_graph_id(self, graph_id):
        """Find all executions for a graph"""
        session = self.db_manager.get_session()
        try:
            executions = session.query(Execution).filter(Execution.graph_id == graph_id).all()
            return map_collection(executions)
        finally:
            session.close()
    
    def update_status(self, execution_id, status):
        """Update the status of an execution"""
        session = self.db_manager.get_session()
        try:
            execution = session.query(Execution).get(execution_id)
            if not execution:
                return False
            
            execution.status = status
            if status in ["COMPLETED", "FAILED", "STOPPED"]:
                execution.completed_at = datetime.now()
                
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def add_result(self, execution_id, node_id, result):
        """Add a result for a node execution"""
        session = self.db_manager.get_session()
        try:
            execution_result = ExecutionResult(
                id=str(uuid.uuid4()),
                execution_id=execution_id,
                node_id=node_id,
                result=result,
                error=None,
                started_at=datetime.now(),
                completed_at=datetime.now(),
                execution_time_ms=0  # Calculate this in a real implementation
            )
            session.add(execution_result)
            session.commit()
            return map_to_domain(execution_result)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def get_results(self, execution_id):
        """Get all results for an execution"""
        session = self.db_manager.get_session()
        try:
            results = session.query(ExecutionResult).filter(
                ExecutionResult.execution_id == execution_id
            ).all()
            return map_collection(results)
        finally:
            session.close()