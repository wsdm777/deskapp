import pytest
from datetime import date
from src.repository.crud.position.position import delete_position
from src.repository.crud.section.schemas import SectionCreate
from src.repository.crud.section.section import (
    add_section,
    delete_section,
    update_section_head,
)
from src.repository.crud.user.schemas import UserCreate, UserLogin, UserSearchParametrs
from src.repository.crud.user.user import (
    change_user_position,
    delete_user,
    get_user_by_email,
    get_users,
    login_user,
    register_user,
    update_user,
)
from src.repository.crud.vacation.schemas import VacationCreate
from test.conftest import fake

from src.repository.crud.vacation.vacation import (
    add_vacation,
    get_all_vacations,
    get_vacation,
)
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


# Тест удаления пользователя
@pytest.mark.asyncio
async def test_delete_user():
    with pytest.raises(AssertionError):
        result = await delete_user(100)
        assert result == 1


# Тест смена должности пользователя
@pytest.mark.asyncio
async def test_change_user_position():
    await change_user_position(
        email="root@example.com", new_position_name=fake.it_job()
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "filter_on_vacation, filter_position",
    [
        (None, None),  # Все пользователи
        (True, None),  # Пользователи в отпуске
        (False, None),  # Пользователи не в отпуске
        (None, fake.it_job()),  # Все пользователи из случайной должности
        (True, fake.it_job()),  # Пользователи в отпуске из случайной должности
        (False, fake.it_job()),  # Пользователи из случайной должности
    ],
)
async def test_get_users(filter_on_vacation, filter_position):
    """
    Тест функции get_users с параметрами filter_on_vacation и filter_position.
    """
    params = UserSearchParametrs(
        filter_on_vacation=filter_on_vacation, filter_position=filter_position
    )
    result = await get_users(params)
    print("\n Тест с параметрами:")
    print(f"filter_on_vacation={filter_on_vacation}, filter_position={filter_position}")
    for row in result:
        print(row)


# Тест просмотра всех отпусков
@pytest.mark.asyncio
async def test_get_all_vacations():
    result = await get_all_vacations()


# Тест просмотра отпуска
@pytest.mark.asyncio
async def test_get_vacation():
    result = await get_vacation(fake.random_int(1, 11))
