from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

NAME = "datab.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{NAME}'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    from  Application.models import User
    return User.query.get(user_id)


from Application import routes


with app.app_context():
    db.create_all()