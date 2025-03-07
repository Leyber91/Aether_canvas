# backend/models/execution_result.py
from sqlalchemy import Column, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from backend.db.sqlalchemy_manager import Base
import uuid
from datetime import datetime

class ExecutionResult(Base):
    __tablename__ = 'execution_results'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey('executions.id'))  # <- fixed datatype here
    node_id = Column(UUID(as_uuid=True), ForeignKey('nodes.id'))
    result = Column(JSON, default={})
    error = Column(JSON)
    execution_time_ms = Column(JSON, default={})
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)

    execution = relationship('Execution', back_populates='execution_results')
