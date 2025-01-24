import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from app.db.base import Base
from app.models.student import Student

class Infomation(Base):
    __tablename__ = "infomation"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    hours_per_day = Column(Integer, nullable=False)
    lessons_per_week = Column(Integer, nullable=False)
    days_of_week = Column(ARRAY(String(10)), nullable=False)
    fee = Column(Float, nullable=False)
    bank_account = Column(String(20), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey(Student.id), nullable=False, index=True)
    student = relationship("Student")
