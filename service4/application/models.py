from application import db


class usernames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_word = db.Column(db.String(30), nullable=False)
    second_word = db.Column(db.String(30), nullable=False)
    user_name = db.column(db.String(30), nullable=False)
    group = db.column(db.string(30), nullable=False)