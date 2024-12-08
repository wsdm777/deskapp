import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.utils.logger import setup_logger
from .config import DB_URL
from .models import Base
from contextlib import asynccontextmanager
from sqlalchemy import event

module_name = os.path.basename(__file__).replace(".py", "")
logger = setup_logger(module_name)

DATABASE_URL = DB_URL

engine = create_async_engine(DATABASE_URL)

sessionfactory = async_sessionmaker(engine, expire_on_commit=False)


@event.listens_for(engine.sync_engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.close()


@asynccontextmanager
async def get_session():
    async with sessionfactory() as session:
        yield session


async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info(f"Database created")


async def drop_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        logger.info(f"Database dropped")
