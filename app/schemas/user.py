from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from uuid import UUID

# User 생성 요청 스키마
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Literal["Teacher", "Student", "Parent"]
    name: str
    phone_number: Optional[str] = None

# User 응답 스키마
class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role: Literal["Teacher", "Student", "Parent"]
    name: str
    phone_number: Optional[str] = None

    class Config:
        from_attributes = True  # Pydantic 모델이 SQLAlchemy의 ORM 객체를 사용할 수 있도록 설정
