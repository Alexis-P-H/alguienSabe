import os
from flask import Blueprint, render_template, request, jsonify
from config import Config_images
from app import db
from app.user_models import User

register = Blueprint('register', __name__)

@register.route('/userForm/', methods=['GET'])
def form():
    return render_template('userForm.html')


@register.route('/postUser/', methods=['POST'])
def postData():
    name = request.form['name']
    address = request.form['address']
    slogan = request.form['slogan']
    contact = request.form['contact']
    image = request.files['image']

    # Guardar la imagen en el sistema de archivos
    if image:
        image_path = os.path.join( Config_images.UPLOAD_FOLDER, image.filename)
        db_uri = image_path
        db_uri = db_uri.replace("D:\\Proyectos\\personal\\apirestFlaskSql\\app/static/", "")
        print("URL formateada:", db_uri)
        image.save(image_path)
    else:
        image_path = None

    data = User(username = name,
        direction = address,
        slogan= slogan,
        contacto= contact,
        image_user = db_uri)
    
    db.session.add(data)
    db.session.commit()

    return render_template('home.html')

@register.route('/putUser/<int:id>', methods=['PUT'])
def putData():
    pass
