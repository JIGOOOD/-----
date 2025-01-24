import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.lesson import Lesson

class Homework(Base):
    __tablename__ = "homework"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    content = Column(String(255), nullable=False)
    completed = Column(Boolean, nullable=False)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey(Lesson.id), nullable=False, index=True)
    lesson = relationship("Lesson")
