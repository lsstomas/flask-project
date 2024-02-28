from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.products import product_bp
from src.users import user_bp

from dotenv import load_dotenv
import os


load_dotenv()


def create_app():
    app = Flask(__name__)

    # Configurações da aplicação
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Componentes da aplicação
    db = SQLAlchemy()
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    # Registrar as blueprints
    app.register_blueprint(user_bp, url_prefix="/")
    app.register_blueprint(product_bp, url_prefix="/produtos")

    return app
