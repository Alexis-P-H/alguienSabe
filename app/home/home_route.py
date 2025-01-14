from flask import Blueprint, render_template, jsonify
from app import db
from app.user_models import User

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home.html')

@home.route('/users/', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = [
        {
            'id': user.id,
            'username': user.username,
            'direction': user.direction,
            'slogan': user.slogan,
            'contacto': user.contacto,
            'image_user': user.image_user
        }
        for user in users
    ]
    return jsonify(users_list)
