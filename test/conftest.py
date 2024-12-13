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
        ]
        return self.random_element(it_departments)


class EmailProvider(BaseProvider):
    def get_email(self):
        emails = [
            "ivanov@mail.ru",
            "petrov@yandex.ru",
            "sidorov@gmail.com",
            "mikhailov@outlook.com",
            "alexeev@hotmail.com",
            "nikolaev@icloud.com",
            "egorov@gmail.com",
            "stepanov@zoho.com",
            "kuznetsov@aol.com",
            "vasiliev@protonmail.com",
        ]
        return self.random_element(emails)


class ITJobProvider(BaseProvider):
    def it_job(self):
        it_jobs = [
            "Разработчик программного обеспечения",
            "Системный администратор",
            "Администратор баз данных",
            "Специалист по информационной безопасности",
            "Техподдержка",
            "Аналитик данных",
            "Разработчик мобильных приложений",
            "DevOps инженер",
            "Архитектор решений",
            "IT менеджер",
        ]
        return self.random_element(it_jobs)


fake = Faker(locale=("ru_RU"))
fake.add_provider(ITDepartmentProvider)
fake.add_provider(EmailProvider)
fake.add_provider(ITJobProvider)


def add_root():
    return register_user(
        UserCreate(
            email="root@example.com",
            name=fake.first_name_male(),
            surname=fake.last_name_male(),
            hashed_password=fake.password(),
            is_superuser=True,
            birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
            position_name=None,
        )
    )


def add_root_section():
    return add_section(SectionCreate(name="root", head_email="root@example.com"))


def user_create_task(amount):
    return [
        register_user(
            UserCreate(
                email=fake.unique.get_email(),
                name=fake.first_name_male(),
                surname=fake.last_name_male(),
                hashed_password=fake.password(),
                is_superuser=fake.boolean(0),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
                position_name=None,
            )
        )
        for _ in range(amount)
    ]


def section_create_task(amount):
    return [
        add_section(
            SectionCreate(name=fake.unique.it_department(), head_email=fake.get_email())
        )
        for _ in range(amount)
    ]


def position_create_task(amount):
    return [
        add_position(
            PositionCreate(
                name=fake.unique.it_job(), section_name=fake.unique.it_department()
            )
        )
        for _ in range(amount)
    ]


def vacation_create_task(amount):
    return [
        add_vacation(
            VacationCreate(
                giver_email=fake.get_email(),
                receiver_email=fake.get_email(),
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

    root_user = add_root()
    root_section = add_root_section()
    user_create_tasks = user_create_task(10)
    fake.unique.clear()
    section_create_tasks = section_create_task(10)
    fake.unique.clear()
    position_create_tasks = position_create_task(10)
    fake.unique.clear()
    vacation_create_tasks = vacation_create_task(10)

    await asyncio.gather(root_user, *user_create_tasks)
    await asyncio.gather(root_section, *section_create_tasks)
    await asyncio.gather(*position_create_tasks)
    await asyncio.gather(*vacation_create_tasks)


def pytest_sessionstart(session):
    logger.info("Starting database setup")
    asyncio.run(refresh_database())
    logger.info("Finish database setup")
