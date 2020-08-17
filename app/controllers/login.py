from . import controllers

@controllers.route('/login')
def login():
    return 'login page'