from backend.db.sqlalchemy_manager import get_session
from backend.db.model_mappers import map_to_domain, map_to_db
from backend.models.conversation import Conversation
from backend.models.message import Message

class ConversationRepository:
    def find_by_node_id(self, node_id):
        with get_session() as session:
            conversations = session.query(Conversation).filter(Conversation.node_id == node_id).all()
            return [map_to_domain(conv) for conv in conversations]

    def find_by_id(self, conversation_id):
        with get_session() as session:
            conversation = session.get(Conversation, conversation_id)
            return map_to_domain(conversation) if conversation else None

    def create(self, conversation_data):
        with get_session() as session:
            db_conversation = map_to_db(Conversation, conversation_data)
            session.add(db_conversation)
            session.commit()
            session.refresh(db_conversation)
            return map_to_domain(db_conversation)

    def find_messages(self, conversation_id):
        with get_session() as session:
            messages = session.query(Message).filter(Message.conversation_id == conversation_id).all()
            return [map_to_domain(msg) for msg in messages]

    def add_message(self, message_data):
        with get_session() as session:
            db_message = map_to_db(Message, message_data)
            session.add(db_message)
            session.commit()
            session.refresh(db_message)
            return map_to_domain(db_message)
        
    def delete_by_node_id(self, node_id):
        """Delete all conversations for a node"""
        session = get_session()
        try:
            conversations = session.query(Conversation).filter(Conversation.node_id == node_id).all()
            for conversation in conversations:
                # Delete all messages for this conversation first
                session.query(Message).filter(Message.conversation_id == conversation.id).delete()
                # Then delete the conversation
                session.delete(conversation)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            
    # backend/repositories/conversation_repository.py - Add this method
    def delete(self, conversation_id):
        """Delete a conversation and its messages"""
        with get_session() as session:
            # Check if conversation exists
            conversation = session.get(Conversation, conversation_id)
            if not conversation:
                return False
                
            # Delete all messages for this conversation
            session.query(Message).filter(Message.conversation_id == conversation_id).delete()
            
            # Delete the conversation
            session.delete(conversation)
            session.commit()
            return True
