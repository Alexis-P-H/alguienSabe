import datetime
from app import app
from flask import Blueprint, Response, redirect, render_template, jsonify, request
from sqlalchemy.orm import load_only
from app.app import db
from app.user_models import User, Data
import base64

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home.html')

@home.route('/users/', methods=['GET'])
def get_all_users():
    users = User.query.limit(10).all()
    actually_hour = datetime.datetime.now()  # Obtiene la hora actual
    colombia_hour = actually_hour #- datetime.timedelta(hours=5)
    colombia_hour_format = colombia_hour.time()

    def validSatatus(open_time, close_time, hora_actual_colombia):
        open_time = datetime.datetime.strptime(open_time, "%H:%M").time()
        close_time = datetime.datetime.strptime(close_time, "%H:%M").time()
        if open_time < hora_actual_colombia < close_time:
            return True
        elif open_time > hora_actual_colombia and hora_actual_colombia < close_time:
            return True
    
    users_list = []
    for user in users:
        imagen_bs64 = base64.b64encode(user.image_user).decode('utf-8')
        users_list.append({
            'id': user.id,
            'username': user.username,
            'direction': user.direction,
            'slogan': user.slogan,
            'contacto': user.contacto,
            'status' : validSatatus(user.open_time, user.close_time, colombia_hour_format),
            'image_base64' : f"data:image/png;base64,{imagen_bs64}"
        })
    return jsonify(users_list)


@home.route('/image/<int:id>', methods=['GET'])
def call_image(id):
    imagen = User.query.options(load_only(User.image_user)).get(id)

    if not imagen or not imagen.image_user:
        return "Imagen no encontrada", 404

    return Response(imagen.image_user, mimetype='image/jpeg')  # Cambia el mimetype según el formato de la imagen

@home.route("/save-user-info", methods=["POST", "GET"])
def save_user_info():
    data = request.json
    data_db = Data(
        number_visit=request.json['numberVisit'],
        userAgent=request.json['userAgent'],
        screenWidth=request.json['screenWidth'],
        screenHeight=request.json['screenHeight'],
        language=request.json['language'],
        timeZone=request.json['timeZone']
    )
    db.session.add(data_db)
    db.session.commit()

    return jsonify({"message": "Datos almacenados correctamente"}), 200

