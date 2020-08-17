from . import controllers

@controllers.route('/challenge')
def challenge():
    return 'challenge page'