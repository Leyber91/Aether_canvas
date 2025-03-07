import unittest
from backend.db.sqlalchemy_manager import init_db
from backend.repositories.graph_repository import GraphRepository
from backend.services.graph_analysis_service import GraphAnalysisService
from backend.infrastructure.logger import get_logger

class TestIntegrationPhase1And2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()
        cls.graph_repo = GraphRepository()
        cls.analysis_service = GraphAnalysisService()
        cls.logger = get_logger("integration_test")

    def test_graph_lifecycle_integration(self):
        graph_data = {
            "name": "Integration Test Graph",
            "description": "Integration test across phase 1 and 2",
            "layout_data": {},
            "graph_metadata": {}
        }
        # Create
        created_graph = self.graph_repo.create(graph_data)
        self.assertIsNotNone(created_graph)
        graph_id = created_graph['id']
        self.logger.info("Graph creation successful", graph_id=graph_id)

        # Fetch graph for verification (dict form)
        fetched_graph = self.graph_repo.find_by_id(graph_id)
        self.assertEqual(fetched_graph['id'], graph_id)
        self.logger.info("Graph fetch successful", graph_id=graph_id)

        # Fetch ORM graph explicitly for analysis
        graph_orm = self.graph_repo.find_by_id(graph_id, as_dict=False)
        self.assertIsNotNone(graph_orm)  # <-- explicitly corrected here!
        self.logger.info("Graph ORM instance fetched successfully", graph_id=graph_orm.id)

        # Graph analysis (Phase 2)
        cycles = self.analysis_service.detect_cycles(graph_id)
        self.assertIsInstance(cycles, list)
        self.logger.info("Graph analysis successful", graph_id=graph_id, cycles=cycles)

        # Graph update
        updated_graph = self.graph_repo.update(graph_id, {"description": "Updated Integration Test"})
        self.assertEqual(updated_graph['description'], "Updated Integration Test")
        self.logger.info("Graph update successful", graph_id=graph_id)

        # Delete graph
        deletion_success = self.graph_repo.delete(graph_id)
        self.assertTrue(deletion_success)
        self.logger.info("Graph deleted successfully", graph_id=graph_id)

        # Confirm deletion
        self.assertIsNone(self.graph_repo.find_by_id(graph_id))
        self.logger.info("Graph deletion confirmed", graph_id=graph_id)

if __name__ == '__main__':
    unittest.main()
