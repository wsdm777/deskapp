import pytest
from src.repository.crud.position.position import delete_position
from src.repository.crud.section.section import delete_section
from src.repository.crud.user.user import (
    delete_user,
    get_user_by_id,
    update_user,
)
from faker import Faker

fake = Faker(locale=("ru_RU"))


@pytest.mark.asyncio
async def test_update_user():
    await update_user(fake.random_int(1, 10))


@pytest.mark.asyncio
async def test_user_info():
    result = await get_user_by_id(fake.random_int(1, 10))
    print(result)


@pytest.mark.asyncio
async def test_delete_user():
    result = await delete_user(fake.random_int(1, 10))
    assert result == 1


@pytest.mark.asyncio
async def test_delete_user():
    with pytest.raises(AssertionError):
        result = await delete_user(100)
        assert result == 1


@pytest.mark.asyncio
async def test_delete_position():
    result = await delete_position(fake.random_int(1, 10))
    assert result == 1


@pytest.mark.asyncio
async def test_delete_section():
    result = await delete_section(fake.random_int(1, 10))
    assert result == 1
