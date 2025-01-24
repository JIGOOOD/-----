import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Date, Integer
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.student import Student

class Calendar(Base):
    __tablename__ = "calendar"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    date = Column(Date, nullable=False)
    lesson_number = Column(Integer, nullable=False)
    month_number = Column(Integer, nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey(Student.id), nullable=False, index=True)
    student = relationship("Student")
