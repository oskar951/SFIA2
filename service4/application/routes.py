from flask import render_template, request
from application import app, db
import requests
from application.models import usernames



@app.route('/bothwords', methods=['GET', 'POST'])
def username():
    firstword = requests.get('http://service2:5001/word').text
    secondword = requests.get('http://service3:5002/word').text
    response = firstword + secondword
    
    if secondword == 'Dude':
        addUsername =  usernames (
            first_word = firstword,
            second_word = secondword,
            user_name = response,
            group = "The Dudes"

        )
        db.session.add(addUsername)
        db.session.commit()
        return "your username is:" + " " + response + " " + "Your group is The Dudes"

    elif secondword == 'Company':
        addUsername =  usernames (
            first_word = firstword,
            second_word = secondword,
            user_name = response,
            group = "The Company"

        )
        db.session.add(addUsername)
        db.session.commit()
        return "your username is:" + " " + response + " " + "Your group is The Company"


    elif secondword == 'Beast':
        addUsername =  usernames (
            first_word = firstword,
            second_word = secondword,
            user_name = response,
            group = "The Beasts"

        )
        db.session.add(addUsername)
        db.session.commit()
        return "your username is:" + " " + response + " " + "Your group is The Beasts"


    elif secondword == 'Croc':
        addUsername =  usernames (
            first_word = firstword,
            second_word = secondword,
            user_name = response,
            group = "The Crocs"

        )
        db.session.add(addUsername)
        db.session.commit()
        return "your username is:" + " " + response + " " + "Your group is The Crocs"


    else:
        return "Error"