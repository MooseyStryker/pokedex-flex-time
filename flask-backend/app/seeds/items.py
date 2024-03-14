from app.models import Item, db
from sqlalchemy.sql import text
#import random


def catch_pokemon_item():
	item1 = Item(
		pokemon_id = 1,
		name = "TM SPICY",
		price = 99,
		happiness =12,
		image_url = "/images/pokemon_super_potion.svg"
	)
	item2 = Item(
		pokemon_id = 2,
		name = "Oran",
		price = 10.22,
		happiness = 44,
		image_url = "/images/pokemon_potion.svg",
	)
	item3 = Item(
		pokemon_id = 3,
		name = "Citrus",
		price = 14,
		happiness = 53,
		image_url = "/images/pokemon_egg.svg",
	)
	item4 = Item(
		pokemon_id = 4,
		name = "Hyper Potion",
		price = 77,
		happiness = 22,
		image_url = "/images/pokemon_egg.svg"
	)
	item5 = Item(
		pokemon_id = 5,
		name = "Potion",
		price = 63,
		happiness = 73,
		image_url = "/images/pokemon_potion.svg",
	)
	item6 = Item(
		pokemon_id = 6,
		name = "Ball",
		price = 23,
		happiness = 12,
		image_url = "/images/pokemon_egg.svg"
	)
	item7 = Item(
		pokemon_id = 7,
		name = "More Item",
		price = 64,
		happiness = 19,
		image_url = "/images/pokemon_super_potion.svg"
	)
	item8 = Item(
		pokemon_id = 8,
		name = "Super Potion",
		price = 13,
		happiness = 91,
		image_url = "/images/pokemon_super_potion.svg"
	)
	item9 = Item(
		pokemon_id = 9,
		name = "Hair Potion",
		price = 10,
		happiness = 5,
		image_url = "/images/pokemon_potion.svg"
	)
	item10 = Item(
		pokemon_id = 10,
		name = "Berry Medicine",
		price = 20,
		happiness = 6,
		image_url = "/images/pokemon_potion.svg"
	)
	all_items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10]
	add_item = [db.session.add(item) for item in all_items]
	db.session.commit()

    #random_generator = random.randint(0,len(all_items) -1)
    #return all_items[random_generator()]

	return add_item


def drop_pokemon_item():
	db.session.execute(text("DELETE FROM pokemon items"))
	db.session.commit()
