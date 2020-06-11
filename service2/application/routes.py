from flask import render_template, request
from application import app
import random


@app.route('/word', methods=['GET'])
def firstword():

	list1 = ['Killer','Boss','The','Bad']

	word1 = random.choice(list1)
	
	return word1