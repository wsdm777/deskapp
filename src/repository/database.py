from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import DB_URL
from .models import Base

DATABASE_URL = DB_URL

engine = create_async_engine(DATABASE_URL)

sessionfabric = async_sessionmaker(engine)


async def get_session():
    async with sessionfabric() as session:
        return session


async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
