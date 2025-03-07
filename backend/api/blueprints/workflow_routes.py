# backend/api/blueprints/workflow_routes.py
from flask import Blueprint, request, jsonify
from backend.services.execution_service import ExecutionService
from backend.infrastructure.logger import get_logger

workflow_routes = Blueprint('workflow_routes', __name__)
logger = get_logger('workflow_routes')
execution_service = ExecutionService()  # Create an instance

@workflow_routes.route('/api/graphs/<graph_id>/execute', methods=['POST'])
def execute_graph(graph_id):
    execution_options = request.get_json() or {}
    try:
        execution = execution_service.execute_workflow(graph_id, execution_options)
        return {"execution_id": execution["id"]}, 202
    except Exception as e:
        logger.error(f"Error executing workflow: {e}")
        return jsonify({"error": str(e)}), 500

@workflow_routes.route('/api/executions/<execution_id>', methods=['GET'])
def get_execution_status(execution_id):
    try:
        status = execution_service.get_execution_status(execution_id)
        if status is None:
            return jsonify({"error": "Execution not found"}), 404
        return {"status": status}, 200
    except Exception as e:
        logger.error(f"Error getting execution status: {e}")
        return jsonify({"error": str(e)}), 500

@workflow_routes.route('/api/executions/<execution_id>/results', methods=['GET'])
def get_execution_results(execution_id):
    try:
        results = execution_service.get_execution_results(execution_id)
        if results is None:
            return jsonify({"error": "Execution not found or not completed"}), 404
        return {"results": results}, 200
    except Exception as e:
        logger.error(f"Error getting execution results: {e}")
        return jsonify({"error": str(e)}), 500

@workflow_routes.route('/api/executions/<execution_id>/stop', methods=['POST'])
def stop_execution(execution_id):
    try:
        stopped = execution_service.stop_execution(execution_id)
        if not stopped:
            return jsonify({"error": "Unable to stop execution"}), 400
        return {"message": "Execution stopped successfully"}, 200
    except Exception as e:
        logger.error(f"Error stopping execution: {e}")
        return jsonify({"error": str(e)}), 500