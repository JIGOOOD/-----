from sqlalchemy.ext.asyncio import create_async_engine
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

async def test_connection():
    engine = create_async_engine(database_url, echo=True)
    async with engine.begin() as conn:
        print("Connection successful!")

asyncio.run(test_connection())
