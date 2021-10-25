from flask import Flask
from flask_sqlalchemy import SQLAlchemy



application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)
