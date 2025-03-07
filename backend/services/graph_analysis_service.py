import networkx as nx
from backend.repositories.graph_repository import GraphRepository

class GraphAnalysisService:

    def build_networkx_graph(self, graph_id):
        graph_repo = GraphRepository()
        graph = graph_repo.find_by_id(graph_id, as_dict=False)  # fetch ORM instance directly
        if not graph:
            raise ValueError("Graph not found.")

        G = nx.DiGraph()

        for node in graph.nodes:
            G.add_node(str(node.id))

        for edge in graph.edges:
            G.add_edge(edge.source_id, edge.target_id)

        return G

    def detect_cycles(self, graph_id):
        G = self.build_networkx_graph(graph_id)
        return list(nx.simple_cycles(G))

    def get_topological_sort(self, graph_id):
        G = self.build_networkx_graph(graph_id)
        if nx.is_directed_acyclic_graph(G):
            return list(nx.topological_sort(G))
        else:
            raise ValueError("Graph contains cycles, cannot perform topological sort.")

