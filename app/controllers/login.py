from . import controllers


@controllers.route('/login/' , methods=['GET','POST'])
def login():
    pass 

@controllers.route('/register/', methods=['GET','POST'])
def register():
    pass
