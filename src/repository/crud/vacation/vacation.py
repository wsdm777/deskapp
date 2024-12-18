from datetime import date
from sqlalchemy import cte, delete, select
from src.repository.crud.vacation.schemas import VacationCreate, VacationInfo
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
            f"Added vacation: giver = {data.giver_email}, receiver = {data.receiver_email}, start = {data.start_date}, end = {data.end_date}"
        )
        return 1


async def get_vacation(vacation_id: int):
    async with get_session() as session:
        query = select(Vacation).where(Vacation.id == vacation_id)
        result = await session.execute(query)
        vacation = result.scalar_one_or_none()

        if vacation is None:
            logger.error(f"Vacaion {vacation_id} not found")
            return 0

        logger.info(f"Selected info vacation {vacation_id}")

        active = False
        if vacation.start_date <= date.today() <= vacation.end_date:
            active = True

        return VacationInfo(
            id=vacation.id,
            giver_email=vacation.giver_email,
            receiver_email=vacation.receiver_email,
            start_date=vacation.start_date,
            end_date=vacation.end_date,
            created_at=vacation.created_date,
            description=vacation.description,
            is_active=active,
        )


async def get_all_vacations(filter_receiver: str = None, filter_giver: str = None):
    async with get_session() as session:
        query = select(Vacation)
        if filter_receiver:
            query = query.filter(Vacation.receiver_email == filter_receiver)
        if filter_giver:
            query = query.filter(Vacation.giver_email == filter_giver)
        result = await session.execute(query)
        result = result.all()

        vacations = []

        for vacation in result:
            vacation_info = await get_vacation(vacation.id)
            vacations.append(vacation_info)

        return vacations
