from flask import Blueprint


bp = Blueprint('pokemon', __name__)



@bp.route('/', methods=["GET"])
def all_pokemon():
    poke_all_the_mons =




@bp.route('/', method=['POST'])
def post_pokemon():
  # form line
    if form.validate_on_submit():
        # model line
        db.session.add()
        db.session.commit()
