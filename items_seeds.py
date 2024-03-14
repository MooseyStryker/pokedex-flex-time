from app.models import Item, db
from random import random, randint

from faker import Faker

fake = Faker()

print('TESTING')
# changed random100 function to random10 since only imported 10 pokemon instead of 100
def random_10():
	return randint(1, 10)

def random_image():
	images = [
		"/images/pokemon_berry.svg",
    	"/images/pokemon_egg.svg",
    	"/images/pokemon_potion.svg",
    	"/images/pokemon_super_potion.svg",
	]

	index = randint(0, len(images) -1)
	return images[index]


def generate_items():
	# while loop and then a for loop
	pokemon_id = 1
	while pokemon_id <= 10:
		# using < 2 in the for loop since 3 is too large for small randomization.. may increase seed data later
		for i in range(2):
			yield {
				"pokemon_id": pokemon_id,
        		"name": fake.name(),
        		"price": random_10(),
        		"happiness": random_10(),
        		"image_url": random_image(),
			}
		pokemon_id += 1
	return i
items = list(generate_items())
print([item for item in items])
# db.session.add()
for item in items:
  print("INSIDE FOR: ", item)
  new_item = Item(	name = item['name'],
					pokemon_id = item['pokemon_id'],
				   	price = item['price'],
		        	happiness = item['happiness'],
		        	image_url = item['image_url'])
  db.session.add(new_item)
  db.session.commit()

#* this seed is completed until more seed data of pokemon is/may-be provided



# items = generate_items()
# for item in items:
# 	db.session.add(Item(**item))
# bd.session.commit()













#gimme space
