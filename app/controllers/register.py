from . import controllers

@controllers.route('/register')
def register():
    return 'register page'