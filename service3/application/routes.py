from flask import render_template, request
from application import app
import random


@app.route('/word', methods=['GET'])
def secondword():

	list = ['Dude','Company','Beast','Croc']
	
	return list[random.randrange(3)]