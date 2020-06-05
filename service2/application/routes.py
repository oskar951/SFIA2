from flask import render_template, request
from application import app
import random


@app.route('/word', methods=['GET'])
def firstword():

	list = ['Killer','Boss','The','Bad']
	
	return list[random.randrange(3)]