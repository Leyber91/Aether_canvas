# backend/services/graph_service.py
from backend.services.graph_crud_service import GraphCRUDService
from backend.services.graph_analysis_service import GraphAnalysisService

class GraphService:
    def __init__(self):
        self.crud_service = GraphCRUDService()
        self.analysis_service = GraphAnalysisService()

    def create_graph(self, graph_data):
        return self.crud_service.create_graph(graph_data)

    def get_graph(self, graph_id):
        return self.crud_service.get_graph(graph_id)

    def update_graph(self, graph_id, updates):
        return self.crud_service.update_graph(graph_id, updates)

    def delete_graph(self, graph_id):
        return self.crud_service.delete_graph(graph_id)

    def analyze_graph(self, graph_id):
        return self.analysis_service.analyze_graph(graph_id)