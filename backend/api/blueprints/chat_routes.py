# backend/api/blueprints/chat_routes.py
from flask import Blueprint, request, Response, stream_with_context, jsonify
from backend.services.conversation_service import ConversationService
from backend.infrastructure.logger import get_logger

logger = get_logger('chat_routes')

chat_routes = Blueprint('chat_routes', __name__)
conversation_service = ConversationService()

@chat_routes.route('/api/nodes/<node_id>/conversations', methods=['GET'])
def get_conversations(node_id):
    conversations = conversation_service.get_conversations(node_id)
    return {"conversations": conversations}, 200

@chat_routes.route('/api/nodes/<node_id>/conversations', methods=['POST'])
def create_conversation(node_id):
    conversation = conversation_service.create_conversation(node_id)
    return jsonify(conversation), 201

@chat_routes.route('/api/conversations/<conversation_id>/messages', methods=['GET'])
def get_messages(conversation_id):
    messages = conversation_service.get_messages(conversation_id)
    return {"messages": messages}, 200

@chat_routes.route('/api/conversations/<conversation_id>/messages', methods=['POST'])
def send_message(conversation_id):
    content = request.json.get('content')
    if not content:
        return jsonify({"error": "Message content required"}), 400
    message = conversation_service.add_message(conversation_id, role='user', content=content)
    return jsonify(message), 201

@chat_routes.route('/api/conversations/<conversation_id>/messages/stream', methods=['GET'])
def stream_messages(conversation_id):
    return Response(
        stream_with_context(conversation_service.stream_conversation(conversation_id)),
        mimetype='text/event-stream'
    )

# backend/api/blueprints/chat_routes.py - Add this endpoint
@chat_routes.route('/api/conversations/<conversation_id>', methods=['DELETE'])
def delete_conversation(conversation_id):
    """Delete a conversation and its messages"""
    try:
        conversation_service.delete_conversation(conversation_id)
        return jsonify({"message": "Conversation deleted successfully"}), 200
    except Exception as e:
        logger.error(f"Error deleting conversation: {e}")
        return jsonify({"error": str(e)}), 500