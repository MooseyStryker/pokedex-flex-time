from flask.cli import AppGroup
from ..models import db
from sqlalchemy.sql import text
from seeds import items_seeds
from seeds import pokemon_seeds as poke_seeds
from seeds import type_seeds
from pokemon_seeds import catch_pokemon, drop_them_pokemon
from items_seeds import generate_items
seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
  catch_pokemon()
  generate_items()
  print('If we see this text, we would be seeding pokemon')



@seed_commands.command("undo")
def undo():
   drop_them_pokemon()
   db.session.execute(text("DELETE * FROM pokemon_types"))
   db.session.execute(text("DELETE * FROM items"))
   db.session.commit()
   print("If we see this text, we would be destroying all our data... 💥")
