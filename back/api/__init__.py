from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    flask_bcrypt.init_app(app)
    db.init_app(app)

    jwt.init_app(app)
    with app.app_context():
        # Import Blueprints
        from back.api.views.movies import movies_bp
        from back.api.views.users import users_bp



        # REGISTER ROUTES
        app.register_blueprint(movies_bp, url_prefix="/movies")
        app.register_blueprint(users_bp, url_prefix="/users")




        return app