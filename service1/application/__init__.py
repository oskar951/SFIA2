from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SFIA2DB')
db = SQLAlchemy(app)


from application import routes
