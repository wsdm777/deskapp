import asyncio
from src.repository.crud.position.position import add_position
from src.repository.crud.position.schemas import PositionCreate
from src.repository.crud.section.schemas import SectionCreate
from src.repository.crud.section.section import add_section
from src.repository.crud.user.schemas import UserCreate
from src.repository.crud.user.user import change_user_position, register_user
from src.repository.crud.vacation.schemas import VacationCreate
from src.repository.crud.vacation.vacation import add_vacation
from src.repository.database import drop_database, initialize_database
from faker import Faker
from faker.providers import BaseProvider
from src.utils.logger import logger


class ITDepartmentProvider(BaseProvider):
    def it_department(self):
        it_departments = [
            "Разработка",
            "Безопасность",
            "Тех. поддержка",
            "Сети",
            "Анализа данных",
            "Автоматизации процессов",
            "Mobile разработка",
            "DevOps",
            "Системное администрирование",
            "Проектирования баз данных",
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
            "Разработчик",
            "Системный администратор",
            "Администратор баз данных",
            "Специалист по безопасности",
            "Техподдержка",
            "Аналитик данных",
            "Разработчик мобильных приложений",
            "DevOps",
            "Архитектор решений",
            "IT менеджер",
            "UI/UX дизайнер",
            "Тестировщик",
            "Инженер по автоматизации",
            "Сетевой инженер",
            "Программист веб-приложений",
            "Менеджер проектов в IT",
            "Инженер по машинному обучению",
            "Руководитель отдела разработки",
            "Разработчик игр",
            "Специалист по облачным технологиям",
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
            hashed_password="root",
            is_superuser=True,
            birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
            position_name=None,
        )
    )


def user_create_task(amount):
    return [
        register_user(
            UserCreate(
                email=fake.unique.get_email(),
                name=fake.first_name_male(),
                surname=fake.last_name_male(),
                hashed_password=fake.password(),
                is_superuser=fake.boolean(20),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
                position_name=None,
            )
        )
        for _ in range(amount)
    ]


def user_fill_create_task(amount):
    return [
        register_user(
            UserCreate(
                email=fake.unique.email(),
                name=fake.first_name_male(),
                surname=fake.last_name_male(),
                hashed_password=fake.password(),
                is_superuser=fake.boolean(20),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
                position_name=fake.it_job(),
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
            PositionCreate(name=fake.unique.it_job(), section_name=fake.it_department())
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
                description=None,
            )
        )
        for _ in range(amount)
    ]


def update_position_create_task(amount):
    return [
        change_user_position(
            email=fake.unique.get_email(), new_position_name=fake.it_job()
        )
        for _ in range(amount)
    ]


async def refresh_database():
    await drop_database()
    await initialize_database()

    root_user = add_root()
    user_create_tasks = user_create_task(10)
    fake.unique.clear()
    section_create_tasks = section_create_task(10)
    fake.unique.clear()
    position_create_tasks = position_create_task(20)
    fake.unique.clear()
    vacation_create_tasks = vacation_create_task(10)
    fake.unique.clear()
    update_position_tasks = update_position_create_task(10)
    fake.unique.clear()
    fill_users = user_fill_create_task(20)

    await asyncio.gather(root_user, *user_create_tasks)
    await asyncio.gather(*section_create_tasks)
    await asyncio.gather(*position_create_tasks)
    await asyncio.gather(*vacation_create_tasks)
    await asyncio.gather(*update_position_tasks)
    await asyncio.gather(*fill_users)


def pytest_sessionstart(session):
    logger.info("Starting database setup")
    asyncio.run(refresh_database())
    logger.info("Finish database setup")
