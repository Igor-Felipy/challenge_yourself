from . import controllers

@controllers.route('/challenge/<int:id>/')
def challenge(id):
    return str(id)

@controllers.route('/challenge/<int:id>/', methods=['POST'])
def answer(id):
    pass