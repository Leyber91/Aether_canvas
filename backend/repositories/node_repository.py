# backend/repositories/node_repository.py
from datetime import datetime
from backend.db.sqlalchemy_manager import get_session
from backend.db.model_mappers import map_to_domain, map_to_db
from backend.models.node import Node
from backend.models.conversation import Conversation
from backend.models.message import Message

class NodeRepository:
    def find_by_graph_id(self, graph_id):
        """Find all nodes for a graph"""
        with get_session() as session:
            nodes = session.query(Node).filter(Node.graph_id == graph_id).all()
            return [map_to_domain(node) for node in nodes]
    
    def find_by_id(self, node_id):
        """Find a node by ID"""
        with get_session() as session:
            node = session.get(Node, node_id)
            return map_to_domain(node)
    
    def create(self, node_data):
        """Create a new node"""
        with get_session() as session:
            db_node = map_to_db(Node, node_data)
            session.add(db_node)
            session.commit()
            session.refresh(db_node)
            return map_to_domain(db_node)
    
    def update(self, node_id, updates):
        """Update a node"""
        with get_session() as session:
            node = session.get(Node, node_id)
            if not node:
                return None
                
            for key, value in updates.items():
                if hasattr(node, key):
                    setattr(node, key, value)
            
            session.commit()
            session.refresh(node)
            return map_to_domain(node)
    
    def delete(self, node_id):
        """Delete a node and its associated conversations"""
        with get_session() as session:
            # First, check if the node exists
            node = session.get(Node, node_id)
            if not node:
                return False
            
            # Find all conversations for this node
            conversations = session.query(Conversation).filter(Conversation.node_id == node_id).all()
            
            # For each conversation, delete its messages first
            for conversation in conversations:
                # Delete all messages for this conversation
                session.query(Message).filter(Message.conversation_id == conversation.id).delete()
                
            # Then delete all conversations for this node
            session.query(Conversation).filter(Conversation.node_id == node_id).delete()
            
            # Now delete the node
            session.delete(node)
            session.commit()
            return True