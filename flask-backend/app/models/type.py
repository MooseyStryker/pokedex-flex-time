from .db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class PokemonType(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
type: Mapped[str] = mapped_column(nullable=False)
