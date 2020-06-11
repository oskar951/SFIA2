from flask import render_template, request
from application import app
import random


@app.route('/word', methods=['GET'])
def secondword():

	list2 = ['Dude','Company','Beast','Croc']

	word2 = random.choice(list2)
	
	return word2