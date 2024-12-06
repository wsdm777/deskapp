from sqlalchemy import delete
from src.repository.crud.vacation.schemas import VacationCreate
from src.repository.models import Vacation
from src.repository.database import get_session


async def add_vacation(data: VacationCreate):
    async with get_session() as session:
        new_vacation = Vacation(
            giver_id=data.giver_id,
            receiver_id=data.receiver_id,
            start_date=data.start_date,
            end_date=data.end_date,
            description=data.description,
        )

        session.add(new_vacation)
        await session.commit()

        return {"status": 201}


async def delete_vacation(id: int):
    async with get_session() as session:
        stmt = delete(Vacation).where(Vacation.id == id)

        result = await session.execute(stmt)
        await session.commit()

        return result.rowcount
