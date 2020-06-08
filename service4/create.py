from application import db
from application.models import usernames

db.drop_all()
db.create_all()
