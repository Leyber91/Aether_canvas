# backend/api/blueprints/graph_routes.py
from flask import Blueprint, request, jsonify
from backend.services.graph_service import GraphService
from backend.services.execution_service import ExecutionService
from backend.infrastructure.logger import get_logger

logger = get_logger('graph_routes')
graph_routes = Blueprint('graph_routes', __name__)

graph_service = GraphService()
execution_service = ExecutionService()

@graph_routes.route('/api/graphs', methods=['GET'])
def get_graphs():
    filters = request.args.to_dict()
    graphs = graph_service.get_graphs(filters)
    return jsonify({"graphs": graphs}), 200

@graph_routes.route('/api/graphs/<graph_id>', methods=['GET'])
def get_graph(graph_id):
    graph = graph_service.get_graph_by_id(graph_id)
    if not graph:
        return jsonify({"error": "Graph not found"}), 404
    return jsonify(graph), 200

@graph_routes.route('/api/graphs', methods=['POST'])
def create_graph():
    graph_data = request.get_json()
    graph = graph_service.create_graph(graph_data)
    return jsonify(graph), 201

@graph_routes.route('/api/graphs/<graph_id>', methods=['PUT'])
def update_graph(graph_id):
    updates = request.get_json()
    updated_graph = graph_service.update_graph(graph_id, updates)
    return jsonify(updated_graph), 200

@graph_routes.route('/api/graphs/<graph_id>', methods=['DELETE'])
def delete_graph(graph_id):
    graph_service.delete_graph(graph_id)
    return jsonify({"message": "Graph deleted successfully"}), 200

@graph_routes.route('/api/graphs/<graph_id>/nodes', methods=['POST'])
def create_node(graph_id):
    node_data = request.get_json()
    node = graph_service.create_node(graph_id, node_data)
    return jsonify(node), 201

@graph_routes.route('/api/nodes/<node_id>', methods=['PUT'])
def update_node(node_id):
    updates = request.get_json()
    node = graph_service.update_node(node_id, updates)
    return jsonify(node), 200


@graph_routes.route('/api/graphs/<graph_id>/edges', methods=['POST'])
def create_edge(graph_id):
    edge_data = request.get_json()
    edge = graph_service.create_edge(edge_data['source_id'], edge_data['target_id'], edge_data['edge_type'])
    return jsonify(edge), 201

@graph_routes.route('/api/edges/<edge_id>', methods=['DELETE'])
def delete_edge(edge_id):
    graph_service.delete_edge(edge_id)
    return jsonify({"message": "Edge deleted successfully"}), 200

@graph_routes.route('/api/graphs/<graph_id>/executions', methods=['GET'])
def execution_history(graph_id):
    history = execution_service.get_execution_history(graph_id)
    return jsonify({"history": history}), 200

# backend/api/blueprints/graph_routes.py
@graph_routes.route('/api/nodes/<node_id>', methods=['DELETE'])
def delete_node(node_id):
    try:
        # This should now handle conversation deletion automatically
        graph_service.delete_node(node_id)
        return jsonify({"message": "Node deleted successfully"}), 200
    except Exception as e:
        logger.error(f"Error deleting node: {e}")
        return jsonify({"error": str(e)}), 500