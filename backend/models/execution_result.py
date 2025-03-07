from sqlalchemy import Column, DateTime, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from backend.db.sqlalchemy_manager import Base
import uuid
from datetime import datetime

class ExecutionResult(Base):
    __tablename__ = 'execution_results'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey('executions.id'))
    node_id = Column(UUID(as_uuid=True), ForeignKey('nodes.id'))
    result = Column(JSON, default={})
    error = Column(JSON, nullable=True)
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    execution_time_ms = Column(JSON, nullable=True)
