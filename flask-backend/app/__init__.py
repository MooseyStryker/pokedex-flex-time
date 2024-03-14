# import statement for CSRF
from flask import Flask, render_template
from flask_migrate import flask_migrate
from app.config import Configuration, os
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .routes.pokemon import bp

app = Flask(__name__)

app.config.from_object(Configuration)
app.register_blueprint(bp, url_prefix='/api')
# db.init_app(app)

# Migrate(app, db)


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
