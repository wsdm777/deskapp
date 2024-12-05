from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from .config import DB_URL
from .models import Base
from contextlib import asynccontextmanager

DATABASE_URL = DB_URL

engine = create_async_engine(DATABASE_URL)

sessionfactory = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def get_session():
    async with sessionfactory() as session:
        yield session


async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
