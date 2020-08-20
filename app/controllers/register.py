from . import controllers
from flask import request, render_template
from ..db import register_db
@controllers.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = []
        data.append(request.form.get("email"))
        data.append(request.form.get("name"))
        data.append(request.form.get("nick"))
        data.append(request.form.get("password"))
        register_db.new_user(data)
        
    else:
        return render_template('request.html')
