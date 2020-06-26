from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gstar1525'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://aljweeldmnimuy:2f5caf24c15f5c70cc01cec6323b9ca2b94a89a386324bad9e90cc1fd7f713e8@ec2-52-0-155-79.compute-1.amazonaws.com:5432/d57gp0qri1oj5u'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from quizApp import routes