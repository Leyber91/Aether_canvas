# backend/models/execution.py
from sqlalchemy import Column, String, DateTime, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from backend.db.sqlalchemy_manager import Base
import uuid
from datetime import datetime

class Execution(Base):
    __tablename__ = 'executions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # UUID type
    graph_id = Column(UUID(as_uuid=True), ForeignKey('graphs.id'))         # clearly defined as UUID
    status = Column(String)
    execution_metadata = Column(JSON, default={})
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)

    # Relationship back to Graph (recommended for consistency)
    graph = relationship('Graph', back_populates='executions')  # clearly define relation here
    # executions.py
    execution_results = relationship('ExecutionResult', back_populates='execution', cascade='all, delete-orphan')
