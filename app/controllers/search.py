from . import controllers

@controllers.route('/search', methods=["POST"])
def search():
    return 'search page'