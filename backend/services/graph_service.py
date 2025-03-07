# backend/services/graph_service.py
from backend.services.graph_crud_service import GraphCRUDService
from backend.infrastructure.logger import get_logger

logger = get_logger('graph_service')

class GraphService:
    def __init__(self):
        self.crud_service = GraphCRUDService()
    
    # Graph operations
    def create_graph(self, graph_data):
        """Create a new graph"""
        return self.crud_service.create_graph(graph_data)
    
    def get_graph_by_id(self, graph_id):
        """Get a graph by ID"""
        return self.crud_service.get_graph(graph_id)
    
    def get_graphs(self, filters=None):
        """Get all graphs, optionally filtered"""
        return self.crud_service.get_all_graphs(filters)
    
    def update_graph(self, graph_id, updates):
        """Update a graph"""
        return self.crud_service.update_graph(graph_id, updates)
    
    def delete_graph(self, graph_id):
        """Delete a graph"""
        return self.crud_service.delete_graph(graph_id)
    
    # Node operations
    def create_node(self, graph_id, node_data):
        """Create a new node in a graph"""
        return self.crud_service.create_node(graph_id, node_data)
    
    def get_node(self, node_id):
        """Get a node by ID"""
        return self.crud_service.get_node(node_id)
    
    def get_nodes_by_graph(self, graph_id):
        """Get all nodes for a graph"""
        return self.crud_service.get_nodes_by_graph(graph_id)
    
    def update_node(self, node_id, updates):
        """Update a node"""
        return self.crud_service.update_node(node_id, updates)
    
    def delete_node(self, node_id):
        """Delete a node"""
        return self.crud_service.delete_node(node_id)
    
    # Edge operations
    def create_edge(self, source_id, target_id, edge_type):
        """Create a new edge between nodes"""
        return self.crud_service.create_edge(source_id, target_id, edge_type)
    
    def delete_edge(self, edge_id):
        """Delete an edge"""
        return self.crud_service.delete_edge(edge_id)