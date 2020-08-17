from . import controllers

@controllers.route('/')
def home():
    return 'Home Page blueprint'