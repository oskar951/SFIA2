from flask import render_template, request
from application import app, db
from application.models import usernames
import requests


@app.route('/')
@app.route('/home')
def home():
    usernamesData = usernames.query.all()
    response = requests.get('http://service4:5003/bothwords')
    finalname = response.text
    return render_template('home.html', title="Home Page", userData=usernamesData, finalname = finalname )