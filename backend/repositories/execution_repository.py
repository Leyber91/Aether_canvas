from backend.db.sqlalchemy_manager import get_session
from backend.db.model_mappers import map_to_domain, map_to_db
from backend.models.execution import Execution, ExecutionResult

class ExecutionRepository:
    def find_by_graph_id(self, graph_id):
        with get_session() as session:
            executions = session.query(Execution).filter(Execution.graph_id == graph_id).all()
            return [map_to_domain(execution) for execution in executions]

    def find_by_id(self, execution_id):
        with get_session() as session:
            execution = session.query(Execution).get(execution_id)
            return map_to_domain(execution)

    def create(self, execution_data):
        with get_session() as session:
            db_execution = map_to_db(execution_data)
            session.add(db_execution)
            session.commit()
            session.refresh(db_execution)
            return map_to_domain(db_execution)

    def update_status(self, execution_id, status):
        with get_session() as session:
            execution = session.query(Execution).get(execution_id)
            execution.status = status
            session.commit()
            return map_to_domain(execution)

    def add_result(self, execution_id, node_id, result):
        with get_session() as session:
            db_result = ExecutionResult(
                execution_id=execution_id,
                node_id=node_id,
                result=result
            )
            session.add(db_result)
            session.commit()
            session.refresh(db_result)
            return map_to_domain(db_result)

    def get_results(self, execution_id):
        with get_session() as session:
            results = session.query(ExecutionResult).filter(ExecutionResult.execution_id == execution_id).all()
            return [map_to_domain(r) for r in results]
