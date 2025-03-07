# tests/test_phase2.py
import unittest
from backend.services.graph_crud_service import GraphCRUDService
from backend.db.sqlalchemy_manager import init_db

class TestPhase2Services(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()
        cls.graph_crud_service = GraphCRUDService()

    def test_graph_crud_operations(self):
        graph_data = {'name': 'Test Graph', 'description': 'Graph CRUD operations test', 'graph_metadata': {}}
        created_graph = self.graph_crud_service.create_graph(graph_data)
        self.assertIsNotNone(created_graph)

        fetched_graph = self.graph_crud_service.get_graph(created_graph['id'])
        self.assertEqual(fetched_graph['id'], created_graph['id'])

        updated_graph = self.graph_crud_service.update_graph(created_graph['id'], {'description': 'Updated description'})
        self.assertEqual(updated_graph['description'], 'Updated description')

        delete_success = self.graph_crud_service.delete_graph(created_graph['id'])
        self.assertTrue(delete_success)

if __name__ == '__main__':
    unittest.main()
