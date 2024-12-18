from sqlalchemy import delete, select
from src.repository.crud.position.schemas import PositionCreate, PositionInfo
from src.repository.models import Position
from src.repository.database import get_session
from src.utils.logger import logger
from sqlalchemy.orm import selectinload


async def add_position(data: PositionCreate):
    async with get_session() as session:
        new_position = Position(section_name=data.section_name, name=data.name)

        # Добавление должности в сессию
        session.add(new_position)
        # Сохранение в бд
        await session.commit()
        # Логгер записывает успешное добавление
        logger.info(
            f"Added position: name = {data.name}, section = {data.section_name}"
        )
        return 1


async def delete_position(name: int):
    async with get_session() as session:
        stmt = delete(Position).where(Position.name == name)
        result = await session.execute(stmt)

        # Сохранение изменений в бд
        await session.commit()

        # Логгер записывает успешное создание должности
        logger.info(f"Deleted position: name = {name}")
        return result.rowcount


async def get_position(position_name: str):
    async with get_session() as session:
        query = (
            select(Position)
            .filter(Position.name == position_name)
            .options(selectinload(Position.user))
        )
        result = await session.execute(query)
        position = result.one_or_none()
        if position is None:
            logger.error(f"Position {position_name} not found")
            return 0
        logger.info(f"Selected info position {position_name}")
        return PositionInfo(
            id=position.id,
            name=position.name,
            section_name=position.section_name,
            user=len(position.user),
        )
