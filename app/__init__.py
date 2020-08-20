from flask import Flask 

app = Flask(__name__, template_folder='template',static_folder='statics')


from app.controllers import controllers
app.register_blueprint(controllers)