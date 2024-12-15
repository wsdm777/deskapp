from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import contains_eager, joinedload, selectinload
from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy import and_, case, delete, func, select, update
from src.repository.models import Position, Section, User, Vacation
from src.repository.database import get_session
from src.repository.crud.user.schemas import UserCreate, UserInfo, UserLogin
from src.utils.logger import logger


def hash_password(password: str) -> str:
    # Получение соли
    salt = gensalt()
    # Создание хеша пароля с помощью соли
    hashed_password = hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


async def register_user(data: UserCreate):
    async with get_session() as session:
        # Хеширование введенного пароля
        data.hashed_password = hash_password(data.hashed_password)
        new_user = User(
            email=data.email,
            name=data.name,
            surname=data.surname,
            hashed_password=data.hashed_password,
            is_superuser=data.is_superuser,
            birthday=data.birthday,
            position_name=data.position_name,
        )
        session.add(new_user)
        # Попытка создания нового пользователя
        try:
            await session.commit()
        except IntegrityError:
            logger.error(f"Fail to register user {data.email}")
            return 0
        # При успешном создании пользователя функция вернет 1 и логгер запишет успешное создание
        logger.info(f"Registered user: {data.email}")
        return 1


async def login_user(data: UserLogin):
    async with get_session() as session:

        # Запрос в базу данных на поиск пользователя с указанным email
        result = await session.execute(select(User).where(User.email == data.email))
        user = result.scalar_one_or_none()

        # Если пользователь не найден или хеш пароля не совпал функция возвращает 0 и логгер записывает ошибку
        if user is None or not checkpw(
            data.password.encode("utf-8"), user.hashed_password.encode("utf-8")
        ):
            logger.error(f"Login failed for {data.email}: Invalid email or password")
            return 0

        # При успешном входе в систему функция возвращает 1 и логгер записывает успешный вход в систему
        logger.info(f"Logged in: {data.email}")
        return 1


async def delete_user(email: str):
    async with get_session() as session:
        stmt = delete(User).where(User.email == email)

        result = await session.execute(stmt)
        await session.commit()

        if result.rowcount == 0:
            logger.error(f"User {email} not found")
            return 0

        logger.info(f"Deleted user {result.rowcount}")
        return 1


async def get_user_by_email(user_email):
    async with get_session() as session:
        stmt = (
            select(User, Position.name, Section.name)
            .outerjoin(Position, User.position_name == Position.name)
            .outerjoin(Section, Position.section_name == Section.name)
            .options(selectinload(User.receiver_vacations))
            .filter(User.email == user_email)
        )

        result = await session.execute(stmt)
        result = result.unique().one_or_none()
        if result is None:
            logger.error(f"User {user_email} not found")

        logger.info(f"Selected info user {user_email}")
        user, position_name, section_name = result
        on_vacation = False
        for vacation in user.receiver_vacations:
            if vacation.start_date <= date.today() <= vacation.end_date:
                on_vacation = True

        return UserInfo(
            id=user.id,
            name=user.name,
            surname=user.surname,
            email=user.email,
            joined_at=user.joined_at,
            birthday=user.birthday,
            position_name=position_name,
            section_name=section_name,
            is_on_vacation=on_vacation,
            is_superuser=user.is_superuser,
        )


async def update_user(email: str):
    async with get_session() as session:
        stmt = update(User).where(User.email == email).values(is_superuser=True)

        result = await session.execute(stmt)
        if result.rowcount == 0:
            logger.error(f"User {email} not found")
            return 0

        logger.info(f"Added superuser rules user {email}")
        await session.commit()

        return 1
