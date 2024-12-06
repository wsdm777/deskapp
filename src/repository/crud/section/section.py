from sqlalchemy import delete
from src.repository.crud.section.schemas import SectionCreate
from src.repository.models import Section
from src.repository.database import get_session


async def add_section(data: SectionCreate):
    async with get_session() as session:
        new_section = Section(name=data.name, head_id=data.head_id)

        session.add(new_section)
        await session.commit()

        return {"status": 201}


async def delete_section(id: int):
    async with get_session() as session:
        stmt = delete(Section).where(Section.id == id)

        result = await session.execute(stmt)
        await session.commit()

        return result.rowcount
