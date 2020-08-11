from flask import Flask 

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    pass

@app.route('/challenge/', methods=['GET','POST'])
def newChallenge():
    pass

@app.route('/challenge/<int:id>/', methods=['GET','POST'])
def getChallenge():
    pass

@app.route('/challenge/<int:id>/edit/', methods=['GET','POST'])
def editChallenge():
    pass

@app.route('/profile/<int:id>/', methods=['GET','POST'])
def getProfile():
    pass

@app.route('/profile/<int:id>/edit/', methods=['GET','POST'])
def editProfile():
    pass

@app.route('/search/', methods=['GET','POST'])
def search():
    pass 

@app.route('/login/' , methods=['GET','POST'])
def login():
    pass 

@app.route('/register/', methods=['GET','POST'])
def register():
    pass

if __name__ == "__main__":
    app.run(debug=True)