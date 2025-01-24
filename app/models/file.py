import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.lesson import Lesson

class File(Base):
    __tablename__ = "file"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    file_name = Column(String(50), nullable=True)
    url = Column(String(225), nullable=False)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey(Lesson.id), nullable=False, index=True)
    lesson = relationship("Lesson")
