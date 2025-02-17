from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Inicializa la base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa la base de datos con la aplicación
    db.init_app(app)
    

    # Registrar Blueprints (si los tienes)
    from app.home.home_route import home
    app.register_blueprint(home)
    from app.register.register_route import register
    app.register_blueprint(register)
    from app.administration.administration_routes import administration
    app.register_blueprint(administration)

    return app