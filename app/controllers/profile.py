from . import controllers

@controllers.route('/profile/<int:id>/')
def profile(id):
    return 'profile page'

@controllers.route('/profile/<int:id>/', methods=['POST'])
def edit_profile(id):
    pass