from . import controllers

@controllers.route('/challenge/', methods=['GET','POST'])
def newChallenge():
    pass

@controllers.route('/challenge/<int:id>/', methods=['GET','POST'])
def getChallenge():
    pass

@controllers.route('/challenge/<int:id>/edit/', methods=['GET','POST'])
def editChallenge():
    pass
