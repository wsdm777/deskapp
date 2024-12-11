from datetime import date

from pydantic import BaseModel, EmailStr, model_validator


class VacationCreate(BaseModel):
    giver_email: EmailStr
    receiver_email: EmailStr
    start_date: date
    end_date: date
    description: str | None

    @model_validator(mode="before")
    def check_date(cls, values):
        start_date = values.get("start_date")
        end_date = values.get("end_date")

        if start_date > end_date:
            raise ValueError("the start date must be earlier than the end date")

        return values
