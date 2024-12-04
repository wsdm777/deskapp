import asyncio
from src.repository.crud.auth.auth import create_user_in_db


async def test_create_user():

    await create_user_in_db()
