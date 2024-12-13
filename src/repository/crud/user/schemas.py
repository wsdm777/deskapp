from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    surname: str
    position_name: Optional[str]
    hashed_password: str
    is_superuser: bool
    birthday: date

    class ConfigDict:
        from_attributes = True


class UserInfo(BaseModel):
    id: int
    name: str
    surname: str
    position_name: str | None
    section_name: str | None
    email: EmailStr
    joined_at: date
    birthday: date
    is_on_vacation: bool
    is_superuser: bool

    class ConfigDict:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
