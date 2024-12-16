import pytest
from datetime import date
from src.repository.crud.position.position import delete_position
from src.repository.crud.section.schemas import SectionCreate
from src.repository.crud.section.section import add_section, delete_section
from src.repository.crud.user.schemas import UserCreate, UserLogin
from src.repository.crud.user.user import (
    change_user_position,
    delete_user,
    get_user_by_email,
    get_users,
    login_user,
    register_user,
    update_user,
)
from test.conftest import fake

from src.repository.crud.vacation.vacation import add_vacation
from src.repository.models import Vacation


# Тест входа в аккаунт
@pytest.mark.asyncio
async def test_login_user():
    await login_user(UserLogin(email="root@example.com", password="root"))


# Тест выдачи прав администратора
@pytest.mark.asyncio
async def test_update_user():
    await update_user(fake.get_email())


# Тест просмотра информации о пользователе
@pytest.mark.asyncio
async def test_user_info():
    await get_user_by_email(fake.get_email())


@pytest.mark.asyncio
async def test_delete_user():
    with pytest.raises(AssertionError):
        result = await delete_user(100)
        assert result == 1


@pytest.mark.asyncio
async def test_change_user_position():
    await change_user_position(
        email="root@example.com", new_position_name=fake.it_job()
    )


@pytest.mark.asyncio
async def test_get_all_users():
    result = await get_users()
    for row in result:
        print(row)


@pytest.mark.asyncio
async def test_get_all_users_on_vacation_true():
    result = await get_users(filter_on_vacation=True)
    for row in result:
        print(row)


@pytest.mark.asyncio
async def test_get_all_users_on_vacation_false():
    result = await get_users(filter_on_vacation=False)
    for row in result:
        print(row)


@pytest.mark.asyncio
async def test_get_all_admins():
    result = await get_users(filter_superuser=True)
    for row in result:
        print(row)


@pytest.mark.asyncio
async def test_get_all_common_users():
    result = await get_users(filter_superuser=False)
    for row in result:
        print(row)


@pytest.mark.asyncio
async def test_get_all_common_users_on_vacation():
    result = await get_users(filter_on_vacation=True, filter_superuser=False)
    for row in result:
        print(row)


@pytest.mark.asyncio
async def test_get_all_common_users_not_on_vacation():
    result = await get_users(filter_on_vacation=False, filter_superuser=False)
    for row in result:
        print(row)


@pytest.mark.asyncio
async def test_get_all_admins_on_vacation():
    result = await get_users(filter_on_vacation=True, filter_superuser=True)
    for row in result:
        print(row)


@pytest.mark.asyncio
async def test_get_all_admins_not_on_vacation():
    result = await get_users(filter_on_vacation=False, filter_superuser=True)
    for row in result:
        print(row)
