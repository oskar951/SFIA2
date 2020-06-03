from flask import Flask

app = Flask(__name__)

from api1 import routes
