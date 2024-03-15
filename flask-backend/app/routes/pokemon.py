from flask import Blueprint, request, render_template
from sqlalchemy import select
from app.models.pokemon import Pokemon, db, Item, PokemonType
from app.forms.pokemon_form import PokemonForm
from app.forms.item_form import ItemForm
from flask import jsonify, make_response

pokemon_routes = Blueprint("pokemon", __name__, url_prefix="/api/pokemon")


@pokemon_routes.route("/", methods=["GET"])
def all_pokemon():
    pokemon = {}
    stmt = select(Pokemon).join(PokemonType.pokemen)
    print(stmt)
    for row in db.session.execute(stmt):
        pokemon[row.Pokemon.id] = {
            "name": row.Pokemon.name,
            "number": row.Pokemon.number,
            "attack": row.Pokemon.attack,
            "defense": row.Pokemon.defense,
            "image_url": row.Pokemon.image_url,
            "type": row.Pokemon.type,
            "moves": row.Pokemon.moves,
            "encounter_rate": row.Pokemon.encounter_rate,
            "catch_rate": row.Pokemon.catch_rate,
        }
    pokemon = jsonify([{"pokemon": pokemon}])
    pokemon.headers.add("Access-Control-Allow-Origin", "*")
    # find another name for this? plural of pokemon is still pokemon maybe we can use a unique variable name?
    return pokemon


@pokemon_routes.route("/<int:id>")
def poke_deets(id):
    pokemon = {}
    stmt = select(Pokemon).where(Pokemon.id == id)
    for row in db.session.execute(stmt):
        pokemon[row.Pokemon.id] = {
            "name": row.Pokemon.name,
            "number": row.Pokemon.number,
            "attack": row.Pokemon.attack,
            "defense": row.Pokemon.defense,
            "image_url": row.Pokemon.image_url,
            "type": row.Pokemon.type,
            "moves": row.Pokemon.moves,
            "encounter_rate": row.Pokemon.encounter_rate,
            "catch_rate": row.Pokemon.catch_rate,
        }
    pokemon = jsonify([{"pokemon": pokemon}])
    pokemon.headers.add("Access-Control-Allow-Origin", "*")

    return pokemon


@pokemon_routes.route("/", methods=["GET", "POST"])
def post_pokemon():
    form = PokemonForm
    if form.validate_on_submit():
        pokemon = Pokemon(
            number=form.data.number,
            attack=form.data.attack,
            defense=form.data.defense,
            image_url=form.data.image_url,
            name=form.data.name,
            type=form.data.type,
            moves=form.data.moves,
            encounter_rate=form.data.encounterRate,
            catch_rate=form.data.catchRate,
            captured=form.data.captured,
        )
        db.session.add(pokemon)
        db.session.commit()
        return {"pokemon": pokemon}


@pokemon_routes.route("/<int:id>", methods=["PUT"])
def update_pokemon():
    pass


# All items view equipped to a pokemon
@pokemon_routes.route("/<int:pokemonId>/items", methods=["GET", "POST"])
def all_items(pokemonId):
    stmt = select(Item).join(Item.poke_items)
    res = db.session.execute(stmt)
    items = res.scalars()
    #   return { "items" : items }
    return {"All Items Associated with the Pokemon": items}


# Create items for a pokemon
@pokemon_routes.route("/<int:pokemonId>/items", methods=["GET", "POST"])
def create_items(pokemonId):

    form = ItemForm()

    if request.method == "POST":
        if form.validate_on_submit():
            create_item = Item(
                name=form.data["name"],
                happiness=form.data["happiness"],
                price=form.data["price"],
                imageUrl=form.data["image_url"],
            )
            db.session.add(create_item)
            db.session.commit()

    return {"Edited Items": create_item}


# gimme space
