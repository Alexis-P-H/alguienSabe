from app.app import db
from sqlalchemy import func

from sqlalchemy import UniqueConstraint

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    direction = db.Column(db.String(120), nullable=False)
    slogan = db.Column(db.String(128), nullable=False)
    contacto = db.Column(db.String(40), nullable=False)
    image_user = db.Column(db.String(250), nullable=False)
    open_time = db.Column(db.String(5), nullable=False)
    close_time = db.Column(db.String(5), nullable=False)
    time_register_user = db.Column(db.DateTime, server_default=func.now())

    __table_args__ = (
        UniqueConstraint('username', name='uq_users_username'),
        UniqueConstraint('direction', name='uq_users_direction'),
    )


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number_visit = db.Column(db.Integer, nullable=False)
    userAgent = db.Column(db.String(), nullable=False)
    screenWidth = db.Column(db.Integer, nullable=False)
    screenHeight = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(20), nullable=False)
    timeZone = db.Column(db.String(150), nullable=False)
    fecha_ingreso = db.Column(db.DateTime, server_default=func.now())

    __table_args__ = (
        UniqueConstraint('number_visit', name='uq_data_number_visit'),
        )


"""Comandos para actualizar base de datos
flask db init
flask db migrate -m "Descripción del cambio"
flask db upgrade

with app.app_context():
    db.session.add(nuevo_usuario)
    db.session.commit()

"""
