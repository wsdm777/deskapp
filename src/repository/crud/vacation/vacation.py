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

        # Добавление нового отпуска в сессию
        session.add(new_vacation)

        # Сохранение нового отпуска в бд
        await session.commit()
        logger.info(
            f"Added vacation: giver = {data.giver_email}, receiver = {data.receiver_email}, start date = {data.start_date} end date = {data.end_date}"
        )
        return 1
