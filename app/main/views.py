from flask import render_template
from . import main

@main.route('/')
def index():
    message="<h1> You have correctly created a view function</h1>"
    return message
