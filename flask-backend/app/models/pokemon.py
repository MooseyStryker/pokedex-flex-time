from .db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Pokemon(db.Models):
    __tablename__ = 'pokemon'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    attack: Mapped[int] = mapped_column(nullable=False)
    defense: Mapped[int] = mapped_column(nullable=False)
    imageUrl: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    moves: Mapped[str] = mapped_column(nullable=False)
    encounterRate: Mapped[float] = mapped_column(min=0, max=100)
    catchRate: Mapped[float] = mapped_column(min=0, max=100)
    captured: Mapped[bool] = mapped_column()
