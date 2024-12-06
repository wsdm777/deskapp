import pytest
import pytest_asyncio
from sqlalchemy import Null
from src.repository.crud.position.position import add_position, delete_position
from src.repository.crud.position.schemas import PositionCreate
from src.repository.crud.section.section import add_section, delete_section
from src.repository.crud.section.schemas import SectionCreate
from src.repository.crud.user.user import delete_user, register_user
from src.repository.crud.user.schemas import UserCreate
from src.repository.crud.vacation.schemas import VacationCreate
from src.repository.crud.vacation.vacation import add_vacation, delete_vacation
from src.repository.database import drop_database, initialize_database
from faker import Faker
from faker.providers import BaseProvider


class ITDepartmentProvider(BaseProvider):
    def it_department(self):
        it_departments = [
            "Отдел разработки программного обеспечения",
            "Отдел информационной безопасности",
            "Отдел технической поддержки",
            "Отдел инфраструктуры и сетей",
            "Отдел анализа данных",
        ]
        return self.random_element(it_departments)


fake = Faker(locale=("ru_RU"))
fake.add_provider(ITDepartmentProvider)


@pytest_asyncio.fixture(scope="module", autouse=True)
async def refresh_database():
    await drop_database()
    await initialize_database()


@pytest.mark.asyncio
async def test_create_user():
    user_data = UserCreate(
        email=fake.email(),
        name=fake.first_name_male(),
        surname=fake.last_name_male(),
        hashed_password=fake.password(),
        is_superuser=fake.boolean(20),
        birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
        position_id=None,
    )

    await register_user(user_data)


@pytest.mark.asyncio
async def test_create_section():
    section_data = SectionCreate(name=fake.it_department(), head_id=1)

    await add_section(section_data)


@pytest.mark.asyncio
async def test_create_position():
    position_data = PositionCreate(name=fake.job_male(), section_id=1)

    await add_position(position_data)


@pytest.mark.asyncio
async def test_create_vacation():
    vacation_data = VacationCreate(
        giver_id=1,
        receiver_id=1,
        start_date=fake.date_this_month(after_today=False),
        end_date=fake.date_this_month(before_today=False),
        description=fake.text(60),
    )

    await add_vacation(vacation_data)


@pytest.mark.asyncio
async def test_delete_user():
    result = await delete_user(1)
    assert result == 1


@pytest.mark.asyncio
async def test_delete_position():
    result = await delete_position(1)
    assert result == 1


@pytest.mark.asyncio
async def test_delete_section():
    result = await delete_section(1)
    assert result == 1


@pytest.mark.asyncio
async def test_delete_vacation():
    result = await delete_vacation(1)
    with pytest.raises(AssertionError):
        assert result == 1


# TODO faker test
