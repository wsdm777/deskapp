from datetime import date
from sqlalchemy import Date, ForeignKey, Index, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase): ...


class Vacation(Base):
    __tablename__ = "vacation"
    id: Mapped[int] = mapped_column(primary_key=True)
    giver_id: Mapped[int] = mapped_column(
        ForeignKey(
            "user.id",
            use_alter=True,
            name="fk_vacation_giv_user",
            ondelete="SET NULL",
        ),
        nullable=True,
    )
    receiver_id: Mapped[int] = mapped_column(
        ForeignKey(
            "user.id",
            use_alter=True,
            name="fk_vacation_rev_user",
            ondelete="CASCADE",
        ),
    )
    start_date = mapped_column(Date, default=date.today)
    end_date = mapped_column(Date)
    description: Mapped[str]

    given = relationship(
        "User", back_populates="given_vacations", foreign_keys=[giver_id]
    )

    receiver = relationship(
        "User", back_populates="receiver_vacations", foreign_keys=[receiver_id]
    )

    __table_args__ = (
        Index("ix_vacation_receiver_id", receiver_id),
        Index("ix_vacation_giver_id", giver_id),
        Index("ix_vacation_dates", start_date, end_date),
    )


class Section(Base):
    __tablename__ = "section"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    head_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "user.id", use_alter=True, name="fk_section_user", ondelete="SET NULL"
        ),
        nullable=True,
    )

    head = relationship("User", back_populates="section_headed", foreign_keys=[head_id])

    position = relationship("Position", back_populates="section")


class Position(Base):
    __tablename__ = "position"
    id: Mapped[int] = mapped_column(primary_key=True)
    section_id: Mapped[int] = mapped_column(
        ForeignKey(
            "section.id",
            use_alter=True,
            name="fk_position_section",
            ondelete="SET NULL",
        ),
        nullable=True,
    )
    name: Mapped[str] = mapped_column(nullable=False, index=True)

    section = relationship("Section", back_populates="position")
    user = relationship("User", back_populates="position")


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    position_id: Mapped[int] = mapped_column(
        ForeignKey(
            "position.id", use_alter=True, name="fk_user_position", ondelete="SET NULL"
        ),
        nullable=True,
    )
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    joined_at = mapped_column(Date, default=date.today)
    birthday = mapped_column(Date)

    position = relationship("Position", back_populates="user")

    section_headed = relationship(
        "Section", back_populates="head", foreign_keys=[Section.head_id]
    )

    given_vacations = relationship(
        "Vacation", back_populates="given", foreign_keys=[Vacation.giver_id]
    )
    receiver_vacations = relationship(
        "Vacation", back_populates="receiver", foreign_keys=[Vacation.receiver_id]
    )
    __table_args__ = (Index("ix_user_position_id", position_id),)
