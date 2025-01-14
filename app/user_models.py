from app import db

# Modelo de usuario
class User(db.Model):
    __tablename__ = 'users'  # Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Columna ID primaria
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nombre de usuario
    direction = db.Column(db.String(120), unique=True, nullable=False)  # Correo electrónico
    slogan = db.Column(db.String(128), nullable=False)
    contacto = db.Column(db.String(40), nullable=False)
    image_user = db.Column(db.String(250), nullable=False)

    # Representación para depuración
    def __repr__(self):
        return f'<User {self.username}>'




"""Comandos para actualizar base de datos
flask db init
flask db migrate -m "Descripción del cambio"
flask db upgrade
"""
