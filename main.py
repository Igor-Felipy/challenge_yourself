from flask import Flask 

app = Flask(__name__)



@app.run('/challenge/<int:id>', methods=['GET','POST'])
def challenge():
    pass

@app.run('/profile/<int:id>', methods=['GET','POST'])
def profile():
    pass

@app.run('/login', methods=['GET','POST'])
def login():
    pass

@app.run('/register', methods=['GET','POST'])
def register():
    pass

@app.run('/feed', methods=['GET'])
def feed():
    pass

@app.run('/search', methods=['GET'])
def search():
    pass


if __name__ == '__main__' :
    app.run( debug=True )