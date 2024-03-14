
from app.models import Pokemon, db
# from ..models.pokemon import Pokemon, db
# from models.pokemon import Pokemon, db
# from ..models import db, Pokemon
from sqlalchemy.sql import text


def catch_pokemon():
	pokemon1 = Pokemon(
		number= 1,
    image_url= '/images/pokemon_snaps/1svg',
    name= 'Bulbasaur',
    attack= 49,
    defense= 49,
    type= 'grass',
    moves= ','.join([
          'tackle',
          'vine whip'
        ]),
    catch_rate = 5.00,
    encounter_rate = 12.00,
    captured = True
	)
	pokemon2 = Pokemon(
		  number = 2,
      image_url = '/images/pokemon_snaps/2.svg',
      name = 'Ivysaur',
      attack = 62,
      defense = 63,
      type = 'grass',
      moves =','.join([
          'tackle',
          'vine whip',
          'razor leaf'
        ]),
      catch_rate = 11.00,
      encounter_rate = 12.00,
      captured = True
	)
	pokemon3 = Pokemon(
      number = 3,
      image_url = '/images/pokemon_snaps/3.svg',
      name = 'Venusaur',
      attack = 82,
      defense = 83,
      type = 'grass',
      moves =','.join([
          'tackle',
          'vine whip',
          'razor leaf'
        ]),
      catch_rate = 74.00,
      encounter_rate = 12.00,
    captured = True
	)
	pokemon4 = Pokemon(
		  number = 4,
      image_url = '/images/pokemon_snaps/4.svg',
      name = 'Charmander',
      attack = 52,
      defense = 43,
      type = 'fire',
      moves =','.join([
          'scratch',
          'ember',
          'metal claw'
        ]),
      catch_rate = 20.00,
      encounter_rate = 12.00,
      captured = True
	)
	pokemon5 = Pokemon(
		  number = 5,
      image_url = '/images/pokemon_snaps/5.svg',
      name = 'Charmeleon',
      attack = 64,
      defense = 58,
      type = 'fire',
      moves =','.join([
          'scratch',
          'ember',
          'metal claw',
          'flamethrower'
        ]),
      catch_rate = 4.00,
      encounter_rate = 12.00,
      captured = True
	)
	pokemon6 = Pokemon(
		  number = 6,
      image_url = '/images/pokemon_snaps/6.svg',
      name = 'Charizard',
      attack = 84,
      defense = 78,
      type = 'fire',
      moves =','.join([
          'flamethrower',
          'wing attack',
          'slash',
          'metal claw'
        ]),
      catch_rate = 30.00,
      encounter_rate = 12.00,
      captured = True
	)
	pokemon7 = Pokemon(
		number = 7,
      image_url = '/images/pokemon_snaps/7.svg',
      name = 'Squirtle',
      attack = 48,
      defense = 65,
      type = 'water',
      moves =','.join([
          'tackle',
          'bubble',
          'water gun'
        ]),
      catch_rate = 66.00,
      encounter_rate = 12.00,
      captured = True
	)
	pokemon8 = Pokemon(
      number = 8,
      image_url = '/images/pokemon_snaps/8.svg',
      name = 'Wartortle',
      attack = 63,
      defense = 80,
      type = 'water',
      moves =','.join([
          'tackle',
          'bubble',
          'water gun',
          'bite'
        ]),
      catch_rate = 14.00,
      encounter_rate = 12.00,
      captured = False
	)
	pokemon9 = Pokemon(
		number = 9,
    image_url = '/images/pokemon_snaps/9.svg',
    name = 'Blastoise',
    attack = 83,
    defense = 100,
    type = 'water',
    moves =','.join([
          'hydro pump',
          'bubble',
          'water gun',
          'bite'
      ]),
		catch_rate = 45.00,
    encounter_rate = 12.00,
    captured = False
	)
	pokemon10 = Pokemon(
		number = 10,
    image_url = '/images/pokemon_snaps/10.svg',
    name = 'Caterpie',
    attack = 30,
    defense = 35,
    type = 'bug',
    moves =','.join([
         'tackle'
      ]),
		catch_rate = 6.00,
    encounter_rate = 14.00,
    captured = False
	)
	all_pokemon = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, pokemon7, pokemon8, pokemon9, pokemon10]
	print('\n Testing the first pokemon ... \n', pokemon1)
	add_pokemon = [db.session.add(pokemon) for pokemon in all_pokemon]
	# if all_pokemon:
  #   # create list comprehension for all_pokemon and if DOES NOT include captured to create a captured = false
	# 	pass

	db.session.commit()
	print("-" *5, "all pokemon seeded", "-"*5)
	return all_pokemon


def drop_them_pokemon():
	db.session.execute(text("DELETE FROM pokemon"))
	db.session.commit()
