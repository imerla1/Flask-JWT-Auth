from os import access
from flask_restful import Resource
from flask import request
from models.user import UserModel
from flask_jwt_extended import create_access_token

class UserLogin(Resource):

    def post(self):

        data = request.get_json()
        username, password = data.get("username"), data.get("password")

        
        user = UserModel.find_by_username(username)
        if user and user.password == password:
            access_token = create_access_token(identity=user.id, fresh=True)
            return {
                "access_token": access_token
            }, 200
        else:
            return {
                "message": "Invalid Credentionals"
            }, 401

    
        