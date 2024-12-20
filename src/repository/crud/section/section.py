from sqlalchemy import delete, select, update
from src.repository.crud import vacation
from src.repository.crud.section.schemas import SectionCreate, SectionInfo
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


async def update_section_head(section_name: str, new_head_email):
    async with get_session() as session:
        stmt = (
            update(Section)
            .where(Section.name == section_name)
            .values(head_email=new_head_email)
        )

        result = await session.execute(stmt)

        if result.rowcount == 0:
            logger.error(f"Section {section_name} not found")
            return 0

        logger.info(f"Change head section: new_head = {new_head_email}")
        await session.commit()

        return 1


async def delete_section(section_name: str):
    async with get_session() as session:
        stmt = delete(Section).where(Section.name == section_name)

        result = await session.execute(stmt)

        # Сохранение изменений
        await session.commit()

        # Запрос не затронул ни одну строку функция возвращает 0 и логгер записывает ошибку
        if result.rowcount == 0:
            logger.error(f"Section {section_name} not found")
            return 0

        logger.info(f"Deleted section {section_name}")
        return 1


async def get_section_by_name(section_name: str):
    async with get_session() as session:
        query = select(Section).filter(Section.name == section_name)
        result = await session.execute(query)
        result = result.unique().scalar_one_or_none()
        if result is None:
            logger.error(f"Section {section_name} not found")
            return 0

        return SectionInfo(id=result.id, name=result.name, head_email=result.head_email)


async def get_all_sections():
    async with get_session() as session:
        query = select(Section)
        result = await session.execute(query)
        result = result.scalars().all()

        sections = []

        for section in result:
            sections.append(
                SectionInfo(
                    id=section.id, name=section.name, head_email=section.head_email
                )
            )

        return sections
