from pydantic import BaseModel, EmailStr


class SectionCreate(BaseModel):
    name: str
    head_email: EmailStr | None


class SectionInfo(SectionCreate):
    id: int
