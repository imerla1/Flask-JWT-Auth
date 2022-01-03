from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from db import db
from flask_restful import Api
from resources.user import UserLogin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "HardToGuessString"

api = Api(app)
jwt = JWTManager(app)
CORS(app)


api.add_resource(UserLogin, "/login")

if __name__ == "__main__":
    db = db.init_app(app)
    app.run(debug=True)
