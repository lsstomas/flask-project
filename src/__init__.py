from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)

    # Definir as configurações da aplicação
    app.config.from_object(Config)

    # Registrar rotas da aplicação
    from .routes import init_routes

    init_routes(app)
