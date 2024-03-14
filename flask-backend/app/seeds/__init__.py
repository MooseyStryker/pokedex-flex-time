from flask.cli import AppGroup
from app.models import db
from sqlalchemy.sql import text
from .pokemon_seeds import catch_pokemon, drop_them_pokemon
from .items import catch_pokemon_item, drop_pokemon_item
from .type_seeds import catch_type, drop_them_types

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
  catch_type()
  catch_pokemon()
  catch_pokemon_item()
  print('If we see this text, we would be seeding pokemon')



@seed_commands.command("undo")
def undo():
  drop_them_pokemon()
  drop_pokemon_item()
  drop_them_types()
  print("If we see this text, we would be destroying all our data... 💥")
