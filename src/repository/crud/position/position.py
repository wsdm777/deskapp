import os
from sqlalchemy import delete
from src.repository.crud.position.schemas import PositionCreate
from src.repository.models import Position
from src.repository.database import get_session
from src.utils.logger import setup_logger

module_name = os.path.basename(__file__).replace(".py", "")
logger = setup_logger(module_name)


async def add_position(data: PositionCreate):
    async with get_session() as session:
        new_position = Position(section_id=data.section_id, name=data.name)

        session.add(new_position)
        await session.commit()
        logger.info(f"Added position: name = {data.name}")
        return {"status": 201}


async def delete_position(id: int):
    async with get_session() as session:
        stmt = delete(Position).where(Position.id == id)

        result = await session.execute(stmt)
        await session.commit()

        return result.rowcount
