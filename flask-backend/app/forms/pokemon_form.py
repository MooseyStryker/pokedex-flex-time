from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField, BooleanField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired , NumberRange

types = [
    ("fire", "Fire"),
    ("electric", "Electric"),
    ("normal", "Normal"),
    ("ghost", "Ghost"),
    ("psychic", "Psychic"),
    ("water", "Water"),
    ("bug", "Bug"),
    ("dragon", "Dragon"),
    ("grass", "Grass"),
    ("fighting", "Fighting"),
    ("ice", "Ice"),
    ("flying", "Flying"),
    ("poison", "Poison"),
    ("ground", "Ground"),
    ("rock", "Rock"),
    ("steel", "Steel"),
]

class Pokemon(FlaskForm):
    number = IntegerField("Number" , validators=[DataRequired()])
    attack = IntegerField("Attack" , validators=[DataRequired()])
    defense = IntegerField("Defense" , validators=[DataRequired()])
    image_url = StringField("Image_Url", validators=[DataRequired()])
    name = StringField("Name" , validators=[DataRequired()])
    type = SelectField("Type" , validators=[DataRequired()], choices=types)
    moves = StringField("Moves" , validators=[DataRequired()])
    encounterRate = DecimalField("EncounterRate" , validators=[DataRequired(), NumberRange(min=0, max=100)], default=1.00)
    catchRate = DecimalField("CatchRate" , validators=[DataRequired(), NumberRange(min=0, max=100)], default = 1.00)
    captured = BooleanField("Captured" , validators=[DataRequired()] , default=False)
    submit = SubmitField("Submit")
