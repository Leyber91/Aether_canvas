from backend.repositories.conversation_repository import ConversationRepository

class ConversationService:
    def __init__(self):
        self.conversation_repo = ConversationRepository()

    def create_conversation(self, node_id):
        conversation_data = {'node_id': node_id, 'title': 'New Conversation'}
        return self.conversation_repo.create(conversation_data)

    def get_conversation(self, conversation_id):
        return self.conversation_repo.find_by_id(conversation_id)

    def get_messages(self, conversation_id):
        return self.conversation_repo.find_messages(conversation_id)

    def add_message(self, conversation_id, role, content):
        message_data = {
            'conversation_id': conversation_id,
            'role': role,
            'content': content
        }
        return self.conversation_repo.add_message(message_data)

    def get_conversation_context(self, conversation_id):
        conversation = self.conversation_repo.find_by_id(conversation_id)
        return conversation.metadata.get('context', {})

