from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from hashids import Hashids
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
bcrypt = Bcrypt(app)
hashids_ = Hashids(
    salt=os.environ['HASHIDS_SALT'],
    alphabet='abcdefghijklmnopqrstuvwxyz123456789-_.~'
)


# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQL_DATABASE_URI']
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Models
from vzlink.models.user import User
from vzlink.models.link import Link


# Routes
from vzlink.routes.api import api_routes
from vzlink.errors import errors
