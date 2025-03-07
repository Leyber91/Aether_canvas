from backend.db.sqlalchemy_manager import get_session
from backend.db.model_mappers import map_to_domain, map_to_db
from backend.models.edge import Edge

class EdgeRepository:
    def find_by_graph_id(self, graph_id):
        with get_session() as session:
            edges = session.query(Edge).filter(Edge.graph_id == graph_id).all()
            return [map_to_domain(edge) for edge in edges]

    def create(self, edge_data):
        with get_session() as session:
            db_edge = map_to_db(edge_data)
            session.add(db_edge)
            session.commit()
            session.refresh(db_edge)
            return map_to_domain(db_edge)

    def delete(self, edge_id):
        with get_session() as session:
            edge = session.query(Edge).get(edge_id)
            session.delete(edge)
            session.commit()
            return True
