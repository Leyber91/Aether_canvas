# backend/repositories/graph_repository.py
from datetime import datetime
from sqlalchemy.orm import joinedload
from backend.db.sqlalchemy_manager import get_session
from backend.db.model_mappers import map_to_domain, map_to_db, map_collection
from backend.models.graph import Graph

class GraphRepository:
    def find_all(self, filters=None):
        """Find all graphs, optionally with filters"""
        session = get_session()
        try:
            query = session.query(Graph)
            if filters:
                # Apply filters if provided
                if 'name' in filters:
                    query = query.filter(Graph.name.ilike(f"%{filters['name']}%"))
            
            graphs = query.all()
            return map_collection(graphs)
        finally:
            session.close()
    
    def find_by_id(self, graph_id, load_relationships=False):
        """Find a graph by ID"""
        session = get_session()
        try:
            if load_relationships:
                graph = session.query(Graph).options(
                    joinedload(Graph.nodes),
                    joinedload(Graph.edges)
                ).get(graph_id)
            else:
                graph = session.get(Graph, graph_id)
            
            return map_to_domain(graph)
        finally:
            session.close()
    
    def create(self, graph_data):
        """Create a new graph"""
        session = get_session()
        try:
            db_graph = map_to_db(Graph, graph_data)
            session.add(db_graph)
            session.commit()
            session.refresh(db_graph)
            return map_to_domain(db_graph)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def update(self, graph_id, updates):
        """Update a graph"""
        session = get_session()
        try:
            graph = session.get(Graph, graph_id)
            if not graph:
                return None
            
            for key, value in updates.items():
                if hasattr(graph, key):
                    setattr(graph, key, value)
            
            graph.updated_at = datetime.now()
            session.commit()
            session.refresh(graph)
            return map_to_domain(graph)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def delete(self, graph_id):
        """Delete a graph"""
        session = get_session()
        try:
            graph = session.get(Graph, graph_id)
            if not graph:
                return False
            
            session.delete(graph)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()