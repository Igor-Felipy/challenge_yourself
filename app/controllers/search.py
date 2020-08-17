from . import controllers

@controllers.route('/search')
def search():
    return 'search page'