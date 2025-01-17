from dotenv import load_dotenv
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


load_dotenv()  # .env 파일 로드
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

Base = declarative_base()  #  SQLAlchemy 모델 정의용 베이스 클래스

engine = create_async_engine(DATABASE_URL, echo=True)  # 비동기 SQLAlchemy 엔진 생성 -> PostgreSQL DB와 연결

# 비동기 세션 생성
async_session = sessionmaker(
    bind=engine,  # 생성된 SQLAlchemy 엔진과 세션 연결
    class_=AsyncSession,  # 세션을 비동기로 동작하도록 설정
    autocommit=False,  # 데이터 변경 사항을 명시적으로 커밋할 때만 반영하도록 설정
    autoflush=False,  # 위와 동일
)
