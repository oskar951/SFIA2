from flask import render_template, request
from application import app, db
from application.models import usernames
import requests
import random
import os


@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    usernamesData = usernames.query.all()
    response = requests.get('http://service4:5003/bothwords')
    username = response.text
    return render_template('home.html', title="Home Page", userData=usernamesData, username = username )