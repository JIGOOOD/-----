import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.student import Student
from app.models.calendar import Calendar

class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    learning_content = Column(String(255), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey(Student.id), nullable=False, index=True)
    student = relationship("Student")
    calendar_id = Column(UUID(as_uuid=True), ForeignKey(Calendar.id), nullable=False, index=True)
    calendar = relationship("Calendar")
