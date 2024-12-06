from datetime import date
from bcrypt import gensalt, hashpw
from sqlalchemy import delete, insert
from sqlalchemy.orm import Session
from src.repository.models import User
from src.repository.database import get_session
from src.repository.crud.user.schemas import UserCreate


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

        return {"status": 201}


async def delete_user(id: int):
    async with get_session() as session:
        stmt = delete(User).where(User.id == id)

        result = await session.execute(stmt)
        await session.commit()

        return result.rowcount
