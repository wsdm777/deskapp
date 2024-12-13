from pydantic import BaseModel


class PositionCreate(BaseModel):
    section_name: str
    name: str
