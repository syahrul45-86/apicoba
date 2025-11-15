from models.user_model import User
from config import db
from flask import request, jsonify

def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return jsonify(user.to_dict())

def create_user():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())

def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    data = request.get_json()
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)

    db.session.commit()
    return jsonify(user.to_dict())

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted"}
