from sqlalchemy import Column, String, DateTime, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from backend.db.sqlalchemy_manager import Base
import uuid
from datetime import datetime

class Context(Base):
    __tablename__ = 'contexts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey('conversations.id'))
    source_type = Column(String, nullable=False)
    source_id = Column(UUID(as_uuid=True), nullable=True)
    context_metadata = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
