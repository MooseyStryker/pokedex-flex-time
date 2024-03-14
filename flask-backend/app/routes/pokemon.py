from flask import Blueprint


bp = Blueprint('pokemon', __name__)



@bp.route('/pokemon', methods=["GET"])
def all_pokemon():
    # poke_all_the_mons =
    pass


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
