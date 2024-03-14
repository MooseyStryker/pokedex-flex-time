from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField, BooleanField, DateField, DecimalField, SelectField
from wtforms.validators import DataRequired

class PokeMon(FlaskForm):
    number = IntegerField("Number" , validators=[DataRequired()])
    attack = IntegerField("Attack" , validators=[DataRequired()])
    defense = IntegerField("Defense" , validators=[DataRequired()])
    image_url = StringField("Image_Url", validators=[DataRequired()])
    name = StringField("Name" , validators=[DataRequired()])
    type = SelectField("Type" , validators=[DataRequired()])
    moves = StringField("Moves" , validators=[DataRequired()])
    encounterRate = DecimalField("EncounterRate" , validators=[DataRequired()], default=1.00)
    catchRate = DecimalField("CatchRate" , validators=[DataRequired()], default=1.00)
    captured = BooleanField("Captured" , validators=[DataRequired()] , default=False)
