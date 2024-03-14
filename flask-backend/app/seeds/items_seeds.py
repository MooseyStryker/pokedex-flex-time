# from app import app
# from app.models.items import Item, db
from faker import commerce
from random import random


# changed random100 function to random10 since only imported 10 pokemon instead of 100
def random_10():
	return random.randint(1, 10)

def random_image():
	images = [
		"/images/pokemon_berry.svg",
    "/images/pokemon_egg.svg",
    "/images/pokemon_potion.svg",
    "/images/pokemon_super_potion.svg",
	]

	index = random.randint(0, len(images) -1)

	return images[index]

# this function rather than having asterisks to indicate random generation like in js, just going to make random generation thru python coding
## unsure the choice of using any number under 125, but we will use every number under 10
def generate_items():
	# while loop and then a for loop
	pokemon_id = 1
	while pokemon_id <= 10:
		# using < 2 in the for loop since 3 is too large for small randomization.. may increase seed data later
		for i in range(2):
			yield {
				"pokemon_id": pokemon_id,
        		"name": commerce.product_name(),
        		"price": random_10(),
        		"happiness": random_10(),
        		"image_url": random_image(),
			}
	pokemonId += 1

#* this seed is completed until more seed data of pokemon is/may-be provided
