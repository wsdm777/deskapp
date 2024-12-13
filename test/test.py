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
from faker import Faker

from src.repository.crud.vacation.vacation import add_vacation
from src.repository.models import Vacation

fake = Faker(locale=("ru_RU"))


@pytest.mark.asyncio
async def test_create_user():
    await register_user(
        UserCreate(
            email="123@example.com",
            name=fake.first_name_male(),
            surname=fake.last_name_male(),
            hashed_password="1",
            is_superuser=fake.boolean(100),
            birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
            position_name=None,
        )
    )


@pytest.mark.asyncio
async def test_login_user():
    await login_user(UserLogin(email="123@example.com", password="1"))


@pytest.mark.asyncio
async def test_create_user_vacancy():
    await add_vacation(
        Vacation(
            giver_email="root@example.com",
            receiver_email="123@example.com",
            start_date=fake.date_this_month(before_today=True, after_today=False),
            end_date=fake.date_this_month(before_today=False, after_today=True),
            description=fake.text(60),
        )
    )


@pytest.mark.asyncio
async def test_create_section():
    await add_section(
        SectionCreate(name=fake.it_department(), head_email="root@example.com")
    )


@pytest.mark.asyncio
async def test_update_user():
    await update_user("123@example.com")


@pytest.mark.asyncio
async def test_user_info():
    result = await get_user_by_email("123@example.com")


@pytest.mark.asyncio
async def test_delete_user():
    with pytest.raises(AssertionError):
        result = await delete_user(100)
        assert result == 1
