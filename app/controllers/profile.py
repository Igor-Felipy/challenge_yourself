from . import controllers

@controllers.route('/profile/<int:id>', methods=['GET','POST'])
def profile():
    return "profile"