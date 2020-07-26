from . import controllers

@controllers.route('/feed', methods=['GET'])
def feed():
    return "feed"