# import statement for CSRF
from flask import Flask, render_template
from flask_migrate import Migrate
from app.config import Configuration, os
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .routes.pokemon import pokemon_routes
from .routes.items import item_routes
from .forms.pokemon_form import PokemonForm
from .forms.item_form import ItemForm
from .models import db
from .seeds import seed_commands



app = Flask(__name__)

app.config.from_object(Configuration)
app.register_blueprint(pokemon_routes, url_prefix='/api/pokemon')
app.register_blueprint(item_routes, url_prefix='/items')## cannot change this url_prefix due to item url variety
db.init_app(app)
app.cli.add_command(seed_commands)
migrate = Migrate(app, db)


# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

@app.route('/pokemon/types')
def all_pokemon_types():
    pass
@app.route('/')
def hello():
    return render_template('hello.html')
