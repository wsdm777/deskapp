from sqlalchemy import delete
from src.repository.crud.vacation.schemas import VacationCreate
from src.repository.models import Vacation
from src.repository.database import get_session
from src.utils.logger import logger


async def add_vacation(data: VacationCreate):
    async with get_session() as session:
        new_vacation = Vacation(
            giver_email=data.giver_email,
            receiver_email=data.receiver_email,
            start_date=data.start_date,
            end_date=data.end_date,
            description=data.description,
        )

        session.add(new_vacation)
        await session.commit()
        logger.info(
            f"Added vacation: giver = {data.giver_email}, receiver = {data.receiver_email}, start date = {data.start_date} end date = {data.end_date}"
        )
        return {"status": 201}


async def delete_vacation(id: int):
    async with get_session() as session:
        stmt = delete(Vacation).where(Vacation.id == id)

        result = await session.execute(stmt)
        await session.commit()

        return result.rowcount
