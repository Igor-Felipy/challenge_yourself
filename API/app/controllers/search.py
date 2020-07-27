from . import controllers


@controllers.route('/search', methods=['GET'])
def search():
    return "search"