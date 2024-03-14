from .db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Table, ForeignKey, Integer
from typing import List

pokemon_typing = Table('pokemon_typing', db.Model.metadata,
    db.Column('pokemon_id', ForeignKey("pokemon.id")),
    db.Column('pokemontype_id', ForeignKey("pokemontype.id"))
)


class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    attack: Mapped[int] = mapped_column(nullable=False)
    defense: Mapped[int] = mapped_column(nullable=False)
    imageUrl: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    types: Mapped[List["PokemonType"]] = relationship(
        "PokemonType",
        secondary=pokemon_typing,
        back_populates="pokemons"
    )
    moves: Mapped[str] = mapped_column(String(255), nullable=False)
    encounterRate: Mapped[float] = mapped_column()
    catchRate: Mapped[float] = mapped_column()
    captured: Mapped[bool] = mapped_column()


class PokemonType(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  type: Mapped[str] = mapped_column(nullable=False)
  pokemons: Mapped[List["Pokemon"]] = relationship(
    "Pokemon",
    secondary=pokemon_typing,
    back_populates="types"
  )
