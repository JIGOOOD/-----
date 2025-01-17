from sqlalchemy.exc import SQLAlchemyError
from app.db.base import async_session

async def get_db():
    try:
        async with async_session() as session:
            yield session
    except SQLAlchemyError as e:
        print(f"DB connection error: {e}")
        raise e