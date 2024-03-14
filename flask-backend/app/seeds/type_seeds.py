from app.models import PokemonType, db
from sqlalchemy.sql import text


types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
];

def catch_type():
  for type in types:
    new_type = PokemonType(
      type = type
    )
    db.session.add(new_type)
  db.session.commit()


def drop_them_types():
	db.session.execute(text("DELETE FROM pokemon_type"))
	db.session.commit()
