

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

login_manager = LoginManager()


app = Flask(__name__)
app.config["SECRET_KEY"]='mysecretkey'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///login.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


login_manager.init_app(app)
login_manager.login_view = 'login'




