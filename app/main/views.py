from flask import render_template
from . import main
#extenstion for secured routes
from flask_login import login_required

@main.route('/')
def index():
    message="You have correctly created a view function"
    return render_template('index.html', message=message)
