from flask import Blueprint, request
from sqlalchemy import select
from app.models.pokemon import Pokemon, db, Item
from app.forms.pokemon_form import PokemonForm
from app.forms.item_form import ItemForm

pokemon_routes = Blueprint('pokemon', __name__, url_prefix="/pokemon")




@pokemon_routes.route('/', methods=["GET"])
def all_pokemon():
   stmt = select(Pokemon)
   row = db.session.execute(stmt)
   pokemon = row.scalars() #find another name for this? plural of pokemon is still pokemon maybe we can use a unique variable name?
   return {"All the Pokes": pokemon}


@pokemon_routes.route('/<int:id>')
def poke_deets(id):
   stmt = select(Pokemon).where(Pokemon.id ==id)
   row = db.session.execute(stmt)
   pokemon = row.scalars()
   return {"pokemon details": pokemon}



@pokemon_routes.route('/', methods=['GET', 'POST'])
def post_pokemon():
  form = PokemonForm
  if form.validate_on_submit():
        pokemon = Pokemon(
           number = form.data.number,
           attack = form.data.attack,
           defense = form.data.defense,
           image_url = form.data.image_url,
           name = form.data.name,
           type = form.data.type,
           moves = form.data.moves,
           encounter_rate = form.data.encounterRate,
           catch_rate = form.data.catchRate,
           captured = form.data.captured
           )
        db.session.add(pokemon)
        db.session.commit()
        return { "pokemon":  pokemon }


@pokemon_routes.route('/<int:id>', methods=['PUT'])
def update_pokemon():
   pass



# All items view equipped to a pokemon
@pokemon_routes.route('/<int:pokemonId>/items', methods=['GET', 'POST'])
def all_items(pokemonId):
  stmt = select(Item).join(Item.poke_items)
  res = db.session.execute(stmt)
  items = res.scalars()
#   return { "items" : items }
  return { "All Items Associated with the Pokemon": items }


# Create items for a pokemon
@pokemon_routes.route('/<int:pokemonId>/items', methods=['GET', 'POST'])
def create_items(pokemonId):

   form = ItemForm()

   if request.method == 'POST':
      if form.validate_on_submit():
         create_item = Item(
            name = form.data['name'],
            happiness = form.data['happiness'],
            price = form.data['price'],
            imageUrl = form.data['image_url'],
         )
         db.session.add(create_item)
         db.session.commit()


   return { "Edited Items": create_item }






# gimme space
