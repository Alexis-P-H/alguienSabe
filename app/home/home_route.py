import datetime
from flask import Blueprint, render_template, jsonify, request
from app.app import db
from app.user_models import User, Data

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home.html')

@home.route('/users/', methods=['GET'])
def get_all_users():
    users = User.query.all()
    hora_actual = datetime.datetime.now().time()  # Obtiene la hora actual

    def validSatatus(open_time, close_time, hora_actual):
        open_time = datetime.datetime.strptime(open_time, "%H:%M").time()
        close_time = datetime.datetime.strptime(close_time, "%H:%M").time()
        if open_time <= hora_actual <= close_time:
            return True
        else:
            return False
        
    users_list = [
        {
            'id': user.id,
            'username': user.username,
            'direction': user.direction,
            'slogan': user.slogan,
            'contacto': user.contacto,
            'image_user': user.image_user,
            'status' : validSatatus(user.open_time, user.close_time, hora_actual)
        }
        for user in users

        
    ]
    return jsonify(users_list)


@home.route("/save-user-info", methods=["POST", "GET"])
def save_user_info():
    data = request.json
    print("Datos recibidos:", data)  # Solo para verificar en la consola

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
