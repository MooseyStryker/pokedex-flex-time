from flask import Blueprint, render_template, redirect
from ..models import db, Item



items = Blueprint('items', __name__)



@items.route('/pokemon/:pokemonId/items')
def all_items():
	pass
   #  poke_all_the_mons =


@items.route('/items/:id', methods=['PUT'])
def edit_item():
	pass


@items.route('/pokemon/:pokemonId/items', methods=['POST'])
def post_items():
	pass
  # form line
   #  if form.validate_on_submit():
        # model line
   #      db.session.add()
   #      db.session.commit()

@items.route('/items/:id', methods=['DELETE'])
def delete_item():
	pass
