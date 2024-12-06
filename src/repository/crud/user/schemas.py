from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    surname: str
    position_id: Optional[int]
    hashed_password: str
    is_superuser: bool
    birthday: date

    class ConfigDict:
        from_attributes = True
