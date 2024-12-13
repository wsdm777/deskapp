from sqlalchemy import delete
from src.repository.crud.section.schemas import SectionCreate
from src.repository.models import Section
from src.repository.database import get_session
from src.utils.logger import logger


async def add_section(data: SectionCreate):
    async with get_session() as session:
        new_section = Section(name=data.name, head_email=data.head_email)

        session.add(new_section)
        await session.commit()
        logger.info(f"Added section: name = {data.name}, head = {data.head_email}")
        return {"status": 201}


async def delete_section(name: str):
    async with get_session() as session:
        stmt = delete(Section).where(Section.name == name)

        result = await session.execute(stmt)
        await session.commit()

        if result.rowcount == 0:
            logger.error(f"Section {name} not found")
            return 0

        logger.info(f"Deleted section {name}")
        return 1


async def get_section_by_name(name: str):
    async with get_session() as session:
        stmt = delete(Section).where(Section.id == id)

        result = await session.execute(stmt)
        await session.commit()
        logger.info(f"Deleted section: id = {id}")
        return result.rowcount
