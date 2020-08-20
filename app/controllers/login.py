from . import controllers
from flask import request, render_template
from ..db import login_db

@controllers.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        data = []
        data.append(request.form.get("email"))
        data.append(request.form.get("password"))
        login_db.login(data)
    else:
        return render_template('login.html')