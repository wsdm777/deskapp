from pydantic import BaseModel


class PositionCreate(BaseModel):
    section_id: int
    name: str
