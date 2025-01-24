import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.student import Student

class Summary(Base):
    __tablename__ = "summary"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    month_number = Column(Integer, nullable=False)
    attitude = Column(String(500), nullable=False)
    lessons_summary = Column(String(800), nullable=False)
    next_plan = Column(String(500), nullable=False)
    notes = Column(String(500), nullable=False)
    created_at = Column(Date, nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey(Student.id), nullable=False, index=True)
    student = relationship("Student")
