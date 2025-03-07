# backend/repositories/graph_repository.py
from backend.db.sqlalchemy_manager import get_session
from backend.db.model_mappers import map_to_domain, map_to_db
from backend.models.graph import Graph
from sqlalchemy.orm import joinedload

class GraphRepository:
# graph_repository.py (no additional changes needed)
    def find_by_id(self, graph_id, as_dict=True):
        with get_session() as session:
            query = session.query(Graph).filter(Graph.id == graph_id)
            if not as_dict:
                graph = query.options(
                    joinedload(Graph.nodes),
                    joinedload(Graph.edges)
                ).first()
                return graph
            graph = session.get(Graph, graph_id)
            return map_to_domain(graph) if graph else None


    def create(self, graph_data):
        with get_session() as session:
            db_graph = map_to_db(Graph, graph_data)
            session.add(db_graph)
            session.commit()
            session.refresh(db_graph)
            return map_to_domain(db_graph)

    def update(self, graph_id, updates):
        with get_session() as session:
            graph = session.get(Graph, graph_id)
            for key, value in updates.items():
                setattr(graph, key, value)
            session.commit()
            session.refresh(graph)
            return map_to_domain(graph)

    def delete(self, graph_id):
        with get_session() as session:
            graph = session.get(Graph, graph_id)
            session.delete(graph)
            session.commit()
            return True
