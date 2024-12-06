from pydantic import BaseModel


class SectionCreate(BaseModel):
    name: str
    head_id: int | None
