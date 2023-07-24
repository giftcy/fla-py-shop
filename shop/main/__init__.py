from flask import Blueprint


# initialising blue print for thus package
main = Blueprint('main', __name__)

# imoorting the routes in this package
from .views import *
