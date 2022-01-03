# User model will be declared here.
from enum import unique
from app import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String) # You should store password hash instead of raw password, for testing.