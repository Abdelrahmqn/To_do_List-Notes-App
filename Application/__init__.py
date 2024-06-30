from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

NAME = "datab.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{NAME}'
db = SQLAlchemy(app)

from Application import routes
