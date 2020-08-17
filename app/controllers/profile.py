from . import controllers

@controllers.route('/profile')
def profile():
    return 'profile page'