from . import main
from flask import render_template



@main.app_errorhander(404)
def page_not_found(e):
    return render_template('errors/404.html'),404

@main.app_errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'),500