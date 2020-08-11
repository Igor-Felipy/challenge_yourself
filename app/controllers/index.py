from . import controllers

@controllers.route('/', methods=['GET'])
def index():
    return 'index'

