from . import controllers
@controllers.route('/challenge/<int:id>', methods=['GET','POST'])
def challenge():
    return "chellenge"