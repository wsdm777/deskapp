from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from .config import DB_URL
from .models import Base

DATABASE_URL = DB_URL

engine = create_async_engine(DATABASE_URL)

sessionfactory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session():
    async with sessionfactory() as session:
        return session


async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
