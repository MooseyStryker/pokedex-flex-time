from flask import Blueprint
from sqlalchemy import select
from app.models.pokemon import Pokemon, db, Item
from app.forms.pokemon_form import PokemonForm

pokemon_routes = Blueprint('pokemon', __name__, url_prefix="/pokemon")




@pokemon_routes.route('/', methods=["GET"])
def all_pokemon():
  stmt = select(Pokemon)
  row = db.session.execute(stmt)
  mad_pokemon = res.scalars() #find another name for this? plural of pokemon is still pokemon maybe we can use a unique variable name?
  return { "pokemon" : mad_pokemon }


@pokemon_routes.route('/<int:id>')
def poke_deets():
   pass



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
        return { "pokemon" : pokemon }


@pokemon_routes.route('/<int:id>', methods=['PUT'])
def update_pokemon():
   pass



# All items view equipped to a pokemon
@pokemon_routes.route('/<int:pokemonId>/items')
def all_items(id):
  stmt = select(Item).join(Item.poke_items)
  res = db.session.execute(stmt)
  items = res.scalars()
#   return { "items" : items }
  return render_template("view_items.html", items=items)


# Create items for a pokemon
@pokemon_routes.route('/<int:pokemonId>/items')
def create_items():
  stmt = select(Item)
  res = db.session.execute(stmt)
  items = res.scalars()
  return { "items" : items }
