import pytest
from src.repository.crud.auth.auth import create_user_in_db
from src.repository.database import drop_database, initialize_database


@pytest.mark.asyncio
async def test_database_refresh():
    await drop_database()
    await initialize_database()


@pytest.mark.asyncio
async def test_create_user():
    await create_user_in_db()
