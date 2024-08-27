from datetime import date, timedelta
from flask import Flask, request, Blueprint, abort, jsonify  # , render_template
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask-psycopg2 import psycopg2
# import dotenv?
# import postgresql?

app = Flask(__name__)

ma = Marshmallow(app)
db = SQLAlchemy(app)


# DB CONNECTION AREA

app.config["SQLALCHEMY_DATABASE_URI"] = ["postgresql://joelvontreifeldt:password@localhost/practice_api"]
# app.config[""] = ["psycopg2 ... / @password / "]




# ROUTING AREA


@app.route("/")
def welcome():
    return "Welcome!"

# @app.route("/users")
# def get_users():
#     body_data = request.get_data("users")

# @app.route("/register")
# @jwt_required
# def register_user():
    # user = User()
