""" CRUD: Create, Read, Update, Delete"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password

async def create_user(db: AsyncSession, user: UserCreate) -> User:
    db_user = User(
        email=user.email,
        password=hash_password(user.password),
        role=user.role,
        name=user.name,
        phone_number=user.phone_number,
    )
    db.add(db_user)  # 세션에 새 객체 추가
    await db.commit()  # 트랜젝션을 db에 저장
    await db.refresh(db_user)  # 세션에서 관리 중인 ORM 객체를 db의 최신 상태로 동기화
    return db_user

async def get_all_users(session: AsyncSession):
    """Fetch all users from the database."""
    result = await session.execute(select(User))
    return result.scalars().all()

async def get_user_by_email(db: AsyncSession, email: str):
    """데이터베이스에서 이메일로 사용자 검색"""
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalar_one_or_none()  # 일치하는 사용자 반환 또는 None