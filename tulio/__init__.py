from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY']='e0128ea6ed00bff947ab3b149765929e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager =LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from tulio import routes