from flask import Blueprint


items = Blueprint('pokemon', __name__)



@items.route('/')
def all_items():
	pass
   #  poke_all_the_mons =




@items.route('/', method=['POST'])
def post_items():
	pass
  # form line
   #  if form.validate_on_submit():
        # model line
   #      db.session.add()
   #      db.session.commit()
