from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired , Length

class ItemForm(FlaskForm):
    happiness = IntegerField("Happiness" , validators=[DataRequired()])
    image_url = StringField("Image_Url" , validators=[DataRequired(), Length(min=0, max=255)])
    name = StringField("Name" , validators=[DataRequired() , Length(min=0, max=255)])
    price = IntegerField("Price" , validators=[DataRequired()])
    pokemon_id = IntegerField("PokemonId" , validators=[DataRequired()])
    submit = SubmitField("Submit")
