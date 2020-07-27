from . import controllers

@controllers.route('/register', methods=['GET','POST'])
def register():
    return "register"