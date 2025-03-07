# backend/services/graph_crud_service.py
import uuid
from datetime import datetime
from backend.repositories.graph_repository import GraphRepository
from backend.repositories.node_repository import NodeRepository
from backend.repositories.edge_repository import EdgeRepository

class GraphCRUDService:
    def __init__(self):
        self.graph_repo = GraphRepository()
        self.node_repo = NodeRepository()
        self.edge_repo = EdgeRepository()
        
    # Graph operations
    def create_graph(self, graph_data):
        """Create a new graph"""
        # Ensure required fields are present
        if 'id' not in graph_data:
            graph_data['id'] = str(uuid.uuid4())
        if 'created_at' not in graph_data:
            graph_data['created_at'] = datetime.now()
        if 'updated_at' not in graph_data:
            graph_data['updated_at'] = datetime.now()
        if 'layout_data' not in graph_data:
            graph_data['layout_data'] = {}
        if 'graph_metadata' not in graph_data:
            graph_data['graph_metadata'] = {}
            
        return self.graph_repo.create(graph_data)
        
    def get_graph(self, graph_id):
        """Get a graph by ID"""
        return self.graph_repo.find_by_id(graph_id)
        
    def get_all_graphs(self, filters=None):
        """Get all graphs, optionally filtered"""
        return self.graph_repo.find_all(filters)
        
    def update_graph(self, graph_id, updates):
        """Update a graph"""
        updates['updated_at'] = datetime.now()
        return self.graph_repo.update(graph_id, updates)
        
    def delete_graph(self, graph_id):
        """Delete a graph"""
        return self.graph_repo.delete(graph_id)
        
    # Node operations - ADD THIS MISSING METHOD
    def create_node(self, graph_id, node_data):
        """Create a new node in a graph"""
        # Ensure required fields are present
        if 'id' not in node_data:
            node_data['id'] = str(uuid.uuid4())
        node_data['graph_id'] = graph_id
        if 'created_at' not in node_data:
            node_data['created_at'] = datetime.now()
        if 'updated_at' not in node_data:
            node_data['updated_at'] = datetime.now()
        if 'position_x' not in node_data:
            node_data['position_x'] = 0.0
        if 'position_y' not in node_data:
            node_data['position_y'] = 0.0
        if 'properties' not in node_data:
            node_data['properties'] = {}
        if 'node_metadata' not in node_data:
            node_data['node_metadata'] = {}
            
        return self.node_repo.create(node_data)
        
    def get_node(self, node_id):
        """Get a node by ID"""
        return self.node_repo.find_by_id(node_id)
        
    def get_nodes_by_graph(self, graph_id):
        """Get all nodes for a graph"""
        return self.node_repo.find_by_graph_id(graph_id)
        
    def update_node(self, node_id, updates):
        """Update a node"""
        updates['updated_at'] = datetime.now()
        return self.node_repo.update(node_id, updates)
        
    def delete_node(self, node_id):
        """Delete a node"""
        return self.node_repo.delete(node_id)
        
    # Edge operations
    def create_edge(self, source_id, target_id, edge_type):
        """Create a new edge between nodes"""
        edge_data = {
            'id': str(uuid.uuid4()),
            'source_id': source_id,
            'target_id': target_id,
            'edge_type': edge_type,
            'edge_metadata': {},
            'created_at': datetime.now()
        }
        return self.edge_repo.create(edge_data)
        
    def delete_edge(self, edge_id):
        """Delete an edge"""
        return self.edge_repo.delete(edge_id)