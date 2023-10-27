import os
from . import create_app
from . import db
from .models.users import User
from flask import jsonify, request, abort

app = create_app(os.getenv('development') or 'default')

@app.route("/user/list", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_json() for user in users])

@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())

@app.route('/user', methods=['POST'])
def create_user():
    if not request.json:
        abort(400)
    user = User(
        name=request.json.get('name'),
        password=request.json.get('password'),
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    if not request.json:
        abort(400)
    user = User.query.get(id)
    if user is None:
        abort(404)
    user.name = request.json.get('name', user.name)
    user.password = request.json.get('password', user.password)
    db.session.commit()
    return jsonify(user.to_json())

@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True})



