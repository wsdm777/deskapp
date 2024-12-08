from datetime import date
import logging
import os
from bcrypt import gensalt, hashpw
from sqlalchemy import and_, case, delete, func, insert, select, update
from sqlalchemy.orm import Session
from src.repository.models import Position, Section, User, Vacation
from src.repository.database import get_session
from src.repository.crud.user.schemas import UserCreate, UserInfo
from src.utils.logger import setup_logger

module_name = os.path.basename(__file__).replace(".py", "")
logger = setup_logger(module_name)


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
        await session.commit()
        logger.info(f"Registered user: {data.email}")
        return {"status": 201}


async def delete_user(id: int):
    async with get_session() as session:
        stmt = delete(User).where(User.id == id)

        result = await session.execute(stmt)
        await session.commit()

        return result.rowcount


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
            raise ValueError

        user, position_name, section_name, on_vacation = result

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
            raise ValueError

        await session.commit()

        return result.rowcount
