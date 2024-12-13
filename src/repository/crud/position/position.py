from sqlalchemy import delete
from src.repository.crud.position.schemas import PositionCreate
from src.repository.models import Position
from src.repository.database import get_session
from src.utils.logger import logger


async def add_position(data: PositionCreate):
    async with get_session() as session:
        new_position = Position(section_name=data.section_name, name=data.name)

        session.add(new_position)
        await session.commit()
        logger.info(
            f"Added position: name = {data.name}, section = {data.section_name}"
        )
        return {"status": 201}


async def delete_position(name: int):
    async with get_session() as session:
        stmt = delete(Position).where(Position.name == name)

        result = await session.execute(stmt)
        await session.commit()
        logger.info(f"Deleted position: name = {name}")
        return result.rowcount
