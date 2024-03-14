# import statement for CSRF
from flask import Flask, render_template
from flask_migrate import Migrate
from app.config import Configuration, os
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .routes.pokemon import bp
from .routes.items import items
from .forms.pokemon_form import Pokemon
from .forms.item_form import Item
from .models import db


app = Flask(__name__)

app.config.from_object(Configuration)
app.register_blueprint(bp, url_prefix='/api')
app.register_blueprint(items, url_prefix='/api')
db.init_app(app)

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
