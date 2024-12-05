import pytest
import pytest_asyncio
from src.repository.crud.auth.auth import create_user_in_db
from src.repository.database import drop_database, initialize_database


@pytest_asyncio.fixture(autouse=True)
async def refresh_database():
    await drop_database()
    await initialize_database()
    yield


@pytest.mark.asyncio
async def test_create_user():
    await create_user_in_db()


# TODO faker test
