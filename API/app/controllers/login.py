from . import controllers


@controllers.route('/login', methods=['GET','POST'])
def login():
    return "login"