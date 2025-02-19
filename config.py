import os
from sqlalchemy import create_engine

class Config:
    # Obtén la cadena de conexión desde una variable de entorno
    DATABASE_URL = os.getenv("DATABASE_URL")
    # Conéctate a la base de datos
    engine = create_engine(DATABASE_URL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False