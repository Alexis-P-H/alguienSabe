import os
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.app import db
from app.user_models import User
from werkzeug.utils import secure_filename

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
    open_tiem = request.form['open_time']
    close_time = request.form['close_time']
    print("Información del formulario", open_tiem, close_time)

    # Guardar la imagen en el sistema de archivos
    if image:
        filename = secure_filename(image.filename)
        print("Esta es una imagen:", filename)
        image_bin = image.read()
        print("Binario de la imagen", image_bin)

    data = User(
        username = name,
        direction = address,
        slogan= slogan,
        contacto= contact,
        image_user = image_bin,
        open_time = open_tiem,
        close_time = close_time
        )
    
    print("información para bd", data)
    
    db.session.add(data)
    db.session.commit()
    
    return redirect(url_for('home.index'))
    

@register.route('/putUser/<int:id>', methods=['PUT'])
def putData():
    pass
