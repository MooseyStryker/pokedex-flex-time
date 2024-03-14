from flask import Blueprint
from sqlalchemy import select
from app.models.pokemon import Pokemon, db

bp = Blueprint('pokemon', __name__, url_prefix="litcity")



@bp.route('/pokemon', methods=["GET"])
def all_pokemon():
  stmt = select(Pokemon)
  res = db.session.execute(stmt)
  pokemons = res.scalars()

@bp.route('/pokemon/:id')
def poke_deets():
   pass


@bp.route('/pokemon', methods=['POST'])
def post_pokemon():
  pass
  # form line
    # if form.validate_on_submit():
    #     # model line
    #     db.session.add()
    #     db.session.commit()


@bp.route('/pokemon/:id', methods=['PUT'])
def update_pokemon():
   pass
