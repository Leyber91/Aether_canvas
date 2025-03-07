# backend/services/graph_crud_service.py
from backend.repositories.graph_repository import GraphRepository

class GraphCRUDService:
    def create_graph(self, graph_data):
        repo = GraphRepository()
        return repo.create(graph_data)

    def get_graph(self, graph_id):
        repo = GraphRepository()
        return repo.find_by_id(graph_id)

    def update_graph(self, graph_id, updates):
        repo = GraphRepository()
        return repo.update(graph_id, updates)

    def delete_graph(self, graph_id):
        repo = GraphRepository()
        return repo.delete(graph_id)