from .db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Item(db.Model):
    __tablename__ = 'item'

    id: Mapped[int] = mapped_column(primary_key=True)
    pokemonId: Mapped[int] = mapped_column(nullable=False)
    happiness: Mapped[int] = mapped_column(nullable=False)
    imageUrl: Mapped[str] = mapped_column(String(255),nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
