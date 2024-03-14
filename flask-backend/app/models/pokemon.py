from .db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, sa
from typing import List




class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    attack: Mapped[int] = mapped_column(nullable=False)
    defense: Mapped[int] = mapped_column(nullable=False)
    image_url: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    moves: Mapped[str] = mapped_column(String(255), nullable=False)
    encounter_rate: Mapped[float] = mapped_column()
    catchRate: Mapped[float] = mapped_column()
    captured: Mapped[bool] = mapped_column()
    types: Mapped[List["PokemonType"]] = relationship(
        "PokemonType",
        secondary=pokemon_typing,
        back_populates="pokemons"
    )
    items: Mapped[List["Item"]] = relationship(back_populates="pokeitems")


class PokemonType(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  type: Mapped[str] = mapped_column(nullable=False)
  pokemons: Mapped[List["Pokemon"]] = relationship(
    "Pokemon",
    secondary=pokemon_typing,
    back_populates="types"
  )

pokemon_typing = db.Table('pokemon_typing',
    sa.Column('pokemon_id', sa.ForeignKey(Pokemon.id), primary_key=True),
    sa.Column('pokemontype_id', sa.ForeignKey(PokemonType.id), primary_key=True)
)

class Item(db.Model):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    pokemon_id: Mapped[int] = mapped_column(ForeignKey("pokemon.id"), nullable=False)
    happiness: Mapped[int] = mapped_column(nullable=False)
    image_url: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    pokeitems: Mapped["Pokemon"] = relationship(back_populates="items")
