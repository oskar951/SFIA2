from flask import Flask

app = Flask(__name__)

from api3 import routes
