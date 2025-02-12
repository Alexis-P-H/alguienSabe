import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # # Clave secreta para la aplicación
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-predeterminada'

    # URI de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'alguienSabe_dataBase.db')

    # Desactivar las notificaciones de cambios en SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False