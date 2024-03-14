from flask import Blueprint, render_template, redirect
from ..models import db, Item
from ..forms.item_form import ItemForm


item_routes = Blueprint('item', __name__, url_prefix="items")


@item_routes.route('/')
def all_items():
  stmt = select(Item)
  res = db.session.execute(stmt)
  items = res.scalars()
  return { "items" : items }


@item_routes.route('/<int:id>', methods=['PUT'])
def edit_item(id):
	 stmt = select(Item).where(Item.id=id)
    row = db.session.execute(st)


@item_routes.route('/pokemon/:pokemonId/items', methods=['POST'])
def post_items():
	pass
  # form line
   #  if form.validate_on_submit():
        # model line
   #      db.session.add()
   #      db.session.commit()

@item_routes.route('/:id', methods=['DELETE'])
def delete_item():
	pass
