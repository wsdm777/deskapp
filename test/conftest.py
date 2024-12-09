import asyncio
from src.repository.crud.position.position import add_position
from src.repository.crud.position.schemas import PositionCreate
from src.repository.crud.section.schemas import SectionCreate
from src.repository.crud.section.section import add_section
from src.repository.crud.user.schemas import UserCreate
from src.repository.crud.user.user import register_user
from src.repository.crud.vacation.schemas import VacationCreate
from src.repository.crud.vacation.vacation import add_vacation, delete_vacation
from src.repository.database import drop_database, initialize_database
from faker import Faker
from faker.providers import BaseProvider
from src.utils.logger import logger


class ITDepartmentProvider(BaseProvider):
    def it_department(self):
        it_departments = [
            "Отдел разработки программного обеспечения",
            "Отдел информационной безопасности",
            "Отдел технической поддержки",
            "Отдел инфраструктуры и сетей",
            "Отдел анализа данных",
            "Отдел автоматизации процессов",
            "Отдел разработки мобильных приложений",
            "Отдел DevOps",
            "Отдел системного администрирования",
            "Отдел проектирования баз данных",
            "Отдел тестирования и качества ПО",
            "Отдел поддержки пользователей",
            "Отдел облачных технологий",
            "Отдел виртуализации и контейнеризации",
            "Отдел разработки веб-приложений",
            "Отдел бизнес-анализа",
            "Отдел интеграции и API",
            "Отдел машинного обучения и искусственного интеллекта",
            "Отдел разработки игр",
            "Отдел безопасности сетевой инфраструктуры",
            "Отдел разработки систем для электронной коммерции",
            "Отдел аналитики и отчетности",
            "Отдел цифровой трансформации",
            "Отдел управления проектами в IT",
        ]
        return self.random_element(it_departments)


fake = Faker(locale=("ru_RU"))
fake.add_provider(ITDepartmentProvider)


def user_create_task(amount):
    return [
        register_user(
            UserCreate(
                email=fake.email(),
                name=fake.first_name_male(),
                surname=fake.last_name_male(),
                hashed_password=fake.password(),
                is_superuser=fake.boolean(0),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
                position_id=None,
            )
        )
        for _ in range(amount)
    ]


def section_create_task(amount):
    return [
        add_section(
            SectionCreate(name=fake.it_department(), head_id=fake.random_int(1, 10))
        )
        for _ in range(amount)
    ]


def position_create_task(amount):
    return [
        add_position(
            PositionCreate(name=fake.job_male(), section_id=fake.random_int(1, 10))
        )
        for _ in range(amount)
    ]


def vacation_create_task(amount):
    return [
        add_vacation(
            VacationCreate(
                giver_id=fake.random_int(1, 10),
                receiver_id=fake.random_int(1, 10),
                start_date=fake.date_this_month(before_today=True, after_today=False),
                end_date=fake.date_this_month(before_today=False, after_today=True),
                description=fake.text(60),
            )
        )
        for _ in range(amount)
    ]


async def refresh_database():
    await drop_database()
    await initialize_database()

    user_create_tasks = user_create_task(10)
    section_create_tasks = section_create_task(10)
    position_create_tasks = position_create_task(10)
    vacation_create_tasks = vacation_create_task(10)

    await asyncio.gather(*user_create_tasks)
    await asyncio.gather(*section_create_tasks)
    await asyncio.gather(*position_create_tasks)
    await asyncio.gather(*vacation_create_tasks)


def pytest_sessionstart(session):
    logger.info("Starting database setup")
    asyncio.run(refresh_database())
    logger.info("Finish database setup")
