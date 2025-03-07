# backend/models/edge.py
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from backend.db.sqlalchemy_manager import Base
import uuid
from datetime import datetime

class Edge(Base):
    __tablename__ = 'edges'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    graph_id = Column(UUID(as_uuid=True), ForeignKey('graphs.id'))  # <- explicitly added
    source_id = Column(UUID(as_uuid=True), ForeignKey('nodes.id'))
    target_id = Column(UUID(as_uuid=True), ForeignKey('nodes.id'))
    edge_type = Column(String, nullable=False)
    edge_metadata = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)

    source = relationship('Node', foreign_keys=[source_id])
    target = relationship('Node', foreign_keys=[target_id])

    graph = relationship('Graph', back_populates='edges')  # <- explicitly added relationship
