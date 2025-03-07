# backend/services/execution_service.py
import uuid
from datetime import datetime
from backend.infrastructure.logger import get_logger
from backend.repositories.execution_repository import ExecutionRepository
from backend.repositories.graph_repository import GraphRepository

logger = get_logger('execution_service')

class ExecutionService:
    def __init__(self):
        self.execution_repo = ExecutionRepository()
        self.graph_repo = GraphRepository()
    
    def execute_workflow(self, graph_id, execution_options=None):
        """
        Execute a workflow for the given graph ID
        """
        logger.info(f"Starting workflow execution for graph '{graph_id}'")
        
        # Check if graph exists
        graph = self.graph_repo.find_by_id(graph_id)
        if not graph:
            logger.error(f"Graph {graph_id} not found")
            raise ValueError(f"Graph {graph_id} not found")
        
        # Create execution record
        execution_data = {
            "id": str(uuid.uuid4()),
            "graph_id": graph_id,
            "status": "PENDING",
            "execution_metadata": execution_options or {},
            "started_at": datetime.now(),
            "completed_at": None
        }
        
        try:
            # Create execution record
            execution = self.execution_repo.create(execution_data)
            
            # Update status to RUNNING
            self.execution_repo.update_status(execution["id"], "RUNNING")
            
            # In a real implementation, we would now:
            # 1. Get the execution order using the graph analysis service
            # 2. Execute each node in order
            # 3. Update the execution status
            
            # For testing purposes, just return the execution info
            logger.info(f"Created execution {execution['id']} for graph {graph_id}")
            return execution
            
        except Exception as e:
            logger.error(f"Failed to execute workflow for graph {graph_id}: {e}")
            raise
    
    def get_execution_status(self, execution_id):
        """
        Get the status of an execution
        """
        execution = self.execution_repo.find_by_id(execution_id)
        if not execution:
            return None
        return execution["status"]
    
    def get_execution_results(self, execution_id):
        """
        Get the results of an execution
        """
        execution = self.execution_repo.find_by_id(execution_id)
        if not execution:
            return None
        
        results = self.execution_repo.get_results(execution_id)
        return {
            "status": execution["status"],
            "started_at": execution["started_at"],
            "completed_at": execution["completed_at"],
            "results": results
        }
    
    def stop_execution(self, execution_id):
        """
        Stop an execution
        """
        execution = self.execution_repo.find_by_id(execution_id)
        if not execution or execution["status"] in ["COMPLETED", "FAILED", "STOPPED"]:
            return False
        
        return self.execution_repo.update_status(execution_id, "STOPPED")
    
    def get_execution_history(self, graph_id):
        """
        Get execution history for a graph
        """
        return self.execution_repo.find_by_graph_id(graph_id)