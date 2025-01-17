import asyncio
from app.db.base import async_session
from app.crud.user import get_all_users

async def main():
    async with async_session() as session:  # 비동기 세션 생성
        # 모든 유저 조회
        users = await get_all_users(session)
        for user in users:
            print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}, PW: {user.password} Role: {user.role}, Phone: {user.phone_number}")

if __name__ == "__main__":
    asyncio.run(main())