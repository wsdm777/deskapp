from datetime import date
from bcrypt import gensalt, hashpw
from sqlalchemy import insert
from sqlalchemy.orm import Session
from src.repository.models import User
from src.repository.database import get_session
from src.repository.crud.auth.schemas import UserCreate


def hash_password(password: str) -> str:
    salt = gensalt()
    hashed_password = hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


async def register_user(data: UserCreate):
    session = await get_session()
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


async def create_user_in_db():
    user_data = UserCreate(
        email="1tes11tfinal123@example.com",
        name="123",
        surname="3232",
        hashed_password="1",
        is_superuser=True,
        birthday=date.today(),
        position_id=None,
    )

    await register_user(user_data)

    print("Пользователь успешно зарегистрирован!")
