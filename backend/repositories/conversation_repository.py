from backend.db.sqlalchemy_manager import get_session
from backend.db.model_mappers import map_to_domain, map_to_db
from backend.models.conversation import Conversation, Message

class ConversationRepository:
    def find_by_node_id(self, node_id):
        with get_session() as session:
            conversations = session.query(Conversation).filter(Conversation.node_id == node_id).all()
            return [map_to_domain(conv) for conv in conversations]

    def find_by_id(self, conversation_id):
        with get_session() as session:
            conversation = session.query(Conversation).get(conversation_id)
            return map_to_domain(conversation)

    def create(self, conversation_data):
        with get_session() as session:
            db_conversation = map_to_db(conversation_data)
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
            db_message = map_to_db(message_data)
            session.add(db_message)
            session.commit()
            session.refresh(db_message)
            return map_to_domain(db_message)
