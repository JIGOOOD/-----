import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from app.db.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(60), nullable=False)  # 비밀번호 해싱 알고리즘 bcrypt 길이 60
    role = Column(String(50), nullable=False, index=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(20), nullable=True)
    