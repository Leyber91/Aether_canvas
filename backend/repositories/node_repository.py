from backend.db.sqlalchemy_manager import get_session
from backend.db.model_mappers import map_to_domain, map_to_db
from backend.models.node import Node

class NodeRepository:
    def find_by_graph_id(self, graph_id):
        with get_session() as session:
            nodes = session.query(Node).filter(Node.graph_id == graph_id).all()
            return [map_to_domain(node) for node in nodes]

    def find_by_id(self, node_id):
        with get_session() as session:
            node = session.query(Node).filter(Node.id == node_id).first()
            return map_to_domain(node)

    def create(self, node_data):
        with get_session() as session:
            db_node = map_to_db(node_data)
            session.add(db_node)
            session.commit()
            session.refresh(db_node)
            return map_to_domain(db_node)

    def update(self, node_id, updates):
        with get_session() as session:
            session.query(Node).filter(Node.id == node_id).update(updates)
            session.commit()
            node = session.query(Node).get(node_id)
            return map_to_domain(node)

    def delete(self, node_id):
        with get_session() as session:
            node = session.query(Node).get(node_id)
            session.delete(node)
            session.commit()
            return True
