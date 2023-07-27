from . import main
from flask import render_template


@main.route("/home")
@main.route("/")
def index():
    return render_template('main/index.html')


@main.route("/about-us")
@main.route("/about")
def about():
    return render_template('main/about.html')
