from flask import render_template, request
from application import app
import requests


@app.route('/bothwords', methods=['GET'])
def username():
    firstword = requests.get('http://service2:5001/word')
    secondword = requests.get('http://service3:5002/word')
    response = firstword.text + secondword.text
    
    if secondword == 'Dude':
        addUsername =  usernames (
            first_word = firstword,
            second_word = secondword,
            user_name = response,
            group = "The Dudes"

        )
        db.session.add(addUsername)
        db.session.commit()
        return response + "Your group is The Dudes"

    elif secondword == 'Company':
        addUsername =  usernames (
            first_word = firstword,
            second_word = secondword,
            user_name = response,
            group = "The Company"

        )
        db.session.add(addUsername)
        db.session.commit()
        return response + "Your group is The Company"


    elif secondword == 'Beast':
        addUsername =  usernames (
            first_word = firstword,
            second_word = secondword,
            user_name = response,
            group = "The Beasts"

        )
        db.session.add(addUsername)
        db.session.commit()
        return response + "Your group is The Beasts"


    elif secondword == 'Croc':
        addUsername =  usernames (
            first_word = firstword,
            second_word = secondword,
            user_name = response,
            group = "The Crocs"

        )
        db.session.add(addUsername)
        db.session.commit()
        return response + "Your group is The Crocs"


    else:
        return "Something went wrong!"