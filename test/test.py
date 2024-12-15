import pytest
from datetime import date
from src.repository.crud.position.position import delete_position
from src.repository.crud.section.schemas import SectionCreate
from src.repository.crud.section.section import add_section, delete_section
from src.repository.crud.user.schemas import UserCreate, UserLogin
from src.repository.crud.user.user import (
    delete_user,
    get_user_by_email,
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
