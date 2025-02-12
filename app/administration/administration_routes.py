from flask import Blueprint, render_template, request, jsonify
from app.app import db
from app.user_models import User

administration = Blueprint('administration', __name__)

@administration.route('/deleteUser/<int:id>', methods=['GET', 'DELETE'])
def deleteUser(id):
    if request.method == 'GET':
        user_for_delete = User.query.get_or_404(id)
        db.session.delete(user_for_delete)
        db.session.commit()
        print(f"Usuario borrado: ", user_for_delete)
    return render_template('home.html')

# @administration.route('/deleteAllUsers/', methods=['GET','DELETE'])
# def deleteAllUsers():
#     if request.method == 'DELETE':
#         meta = db.metadata
#         for table in reversed(meta.sorted_tables):
#             db.session.execute(table.delete())
#         db.session.commit()
#         return "Los usuarios han sido eliminados"
    
#     users = User.query.all()
#     user_list = [
#         {
#             'id': user.id,
#             'username': user.username,
#             'direction': user.direction,
#             'slogan': user.slogan,
#             'contacto': user.contacto,
#             'image_user': user.image_user
#         }
#         for user in users
#     ]
    
#     return jsonify(user_list)