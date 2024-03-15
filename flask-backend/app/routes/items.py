from flask import Blueprint, request
from ..models import db, Item
from ..forms.item_form import ItemForm
from sqlalchemy import select

item_routes = Blueprint('item', __name__)
#url_prefix = /items



@item_routes.route('/<int:id>/update', methods=['GET','POST'])
def edit_item(id):
  stmt = select(Item).where(Item.id == id)
  row = db.session.execute(stmt)
  item = row.scalars()

  form = ItemForm()

  if request.method == 'POST':
    if form.validate_on_submit():
      edit_item = Item(
        name = form.data["name"],
        price = form.data["price"],
        happiness = form.data["happiness"]
      )
      db.session.commit()


  return { "Edited Item": edit_item }

@item_routes.route('/<int:id>', methods=['POST'])
def delete_item(id):
  item_find = select(Item).where(Item.id == id)
  execute_item = db.session.delete(item_find)
  db.session.commit()





#spacee
