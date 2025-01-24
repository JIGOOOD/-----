import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Date
from app.db.base import Base

class Student(Base):
    __tablename__ = "student"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(50), nullable=False, index=True)
    grade = Column(String(50), nullable=False)
    school = Column(String(100), nullable=True)
    address = Column(String(225), nullable=False)
    start_date = Column(Date, nullable=False)
    unique_code = Column(String(10), nullable=False, index=True)
    