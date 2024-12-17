from tkinter import SE
from sqlalchemy import delete, select
from src.repository.crud.section.schemas import SectionCreate
from src.repository.models import Position, Section, User
from src.repository.database import get_session
from src.utils.logger import logger


async def add_section(data: SectionCreate):
    async with get_session() as session:
        new_section = Section(name=data.name, head_email=data.head_email)

        # Добавление отдела в сессию
        session.add(new_section)

        # Сохранение изменений в бд
        await session.commit()

        logger.info(f"Added section: name = {data.name}, head = {data.head_email}")
        return 1


async def delete_section(name: str):
    async with get_session() as session:
        stmt = delete(Section).where(Section.name == name)

        result = await session.execute(stmt)

        # Сохранение изменений
        await session.commit()

        # Запрос не затронул ни одну строку функция возвращает 0 и логгер записывает ошибку
        if result.rowcount == 0:
            logger.error(f"Section {name} not found")
            return 0

        logger.info(f"Deleted section {name}")
        return 1


async def get_section_by_name(section_name: str):
    async with get_session() as session:
        query = (
            select(Section, Position.name)
            .outerjoin(Position, Section.name == Position.section_name)
            .filter(Section.name == section_name)
        )
        result = await session.execute(query)
        result = result.unique().all()
        return result
