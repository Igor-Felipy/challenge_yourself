from flask import Flask 

app = Flask(__name__)

from app.controllers import controllers as controllers_blueprint
app.register_blueprint(controllers_blueprint)