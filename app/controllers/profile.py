from . import controllers

@controllers.route('/profile/<int:id>/', methods=['GET','POST'])
def getProfile():
    pass

@controllers.route('/profile/<int:id>/edit/', methods=['GET','POST'])
def editProfile():
    pass
