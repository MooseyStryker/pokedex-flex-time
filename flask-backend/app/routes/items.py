from flask import Blueprint, render_template, redirect, request
from ..models import db, Item
from ..forms.item_form import ItemForm
from sqlalchemy import select

item_routes = Blueprint('item', __name__)
#url_prefix = /items


@item_routes.route('/<int:id>/update', methods=['GET','POST'])
def edit_item(id):
  stmt = select(Item).where(Item.id == id)
  row = db.session.execute(stmt)
  items = row.scalars()

  form = ItemForm()

  if request.method == 'POST':
    if form.validate_on_submit():
      items.name = form.data["name"]
      items.price = form.data["price"]
      items.happiness = form.data["happiness"]
      db.session.commit()
      return redirect(f"/pokemon/{id}")

  return render_template("post_and_put_item.html", id=id, form=form)

@item_routes.route('/<int:id>', methods=['POST'])
def delete_item(id):
  item_find = select(Item).where(Item.id == id)
  execute_item = db.session.delete(item_find)
  db.session.commit()
  return redirect("/")




#spacee
