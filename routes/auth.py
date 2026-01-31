from flask_restx import Namespace, Resource, fields
from flask import request
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

api = Namespace("auth", description="Authentication APIs")

user_model = api.model("User", {
    "name": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "role": fields.String(required=True, enum=["admin", "receptionist", "customer"])
})

@api.route("/register")
class Register(Resource):
    @api.expect(user_model)
    def post(self):
        data = request.json
        hashed_password = generate_password_hash(data["password"])
        user = User(name=data["name"], email=data["email"], password=hashed_password, role=data["role"])
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201

login_model = api.model("Login", {
    "email": fields.String(required=True),
    "password": fields.String(required=True)
})

@api.route("/login")
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        data = request.json
        user = User.query.filter_by(email=data["email"]).first()
        if user and check_password_hash(user.password, data["password"]):
            return {"message": f"Welcome {user.name}", "role": user.role}, 200
        return {"message": "Invalid credentials"}, 401
