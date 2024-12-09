from datetime import date
from sqlalchemy.exc import IntegrityError
from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy import and_, case, delete, func, select, update
from src.repository.models import Position, Section, User, Vacation
from src.repository.database import get_session
from src.repository.crud.user.schemas import UserCreate, UserInfo, UserLogin
from src.utils.logger import logger


def hash_password(password: str) -> str:
    salt = gensalt()
    hashed_password = hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


async def register_user(data: UserCreate):
    async with get_session() as session:
        data.hashed_password = hash_password(data.hashed_password)
        new_user = User(
            email=data.email,
            name=data.name,
            surname=data.surname,
            hashed_password=data.hashed_password,
            is_superuser=data.is_superuser,
            birthday=data.birthday,
            position_id=data.position_id,
        )
        session.add(new_user)
        try:
            await session.commit()
        except IntegrityError:
            logger.error(f"Fail to register user {data.email}")
            return {"status": 400}
        logger.info(f"Registered user: {data.email}")
        return {"status": 201}


async def login_user(data: UserLogin):
    async with get_session() as session:
        result = await session.execute(select(User).where(User.email == data.email))
        user = result.scalar_one_or_none()

        if user is None or not checkpw(
            data.password.encode("utf-8"), user.hashed_password.encode("utf-8")
        ):
            logger.error(f"Login failed for {data.email}: Invalid email or password")
            return {"msg": "Неверный логин или пароль"}

        logger.info(f"Logged in: {data.email}")
        return await get_user_by_id(user.id)


async def delete_user(id: int):
    async with get_session() as session:
        stmt = delete(User).where(User.id == id)

        result = await session.execute(stmt)
        await session.commit()

        if result.rowcount == 0:
            logger.error(f"User {id} not found")
            return 0

        logger.info(f"Deleted user {result.rowcount}")
        return 1


async def get_user_by_id(user_id):
    async with get_session() as session:
        stmt = (
            select(
                User,
                Position.name,
                Section.name,
                func.max(
                    case(
                        (
                            and_(
                                Vacation.start_date <= date.today(),
                                Vacation.end_date >= date.today(),
                            ),
                            True,
                        ),
                        else_=False,
                    )
                ).label("is_on_vacation"),
            )
            .outerjoin(Vacation, User.id == Vacation.receiver_id)
            .outerjoin(Position, User.position_id == Position.id)
            .outerjoin(Section, Position.section_id == Section.id)
            .filter(User.id == user_id)
            .group_by(User, Position.name, Section.name)
        )

        result = await session.execute(stmt)
        result = result.one_or_none()
        if result is None:
            logger.error(f"User {user_id} not found")

        user, position_name, section_name, on_vacation = result
        logger.info(f"Selected info user {user_id}")
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


async def update_user(id: int):
    async with get_session() as session:
        stmt = update(User).where(User.id == id).values(is_superuser=True)

        result = await session.execute(stmt)
        if result.rowcount is None:
            logger.error(f"User {id} not found")

        logger.info(f"Added superuser rules user {id}")
        await session.commit()

        return result.rowcount
