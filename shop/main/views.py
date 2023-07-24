from . import main


@main.route("/home")
@main.route("/")
def index():
    return 'home'


@main.route("/about-us")
@main.route("/about")
def about():
    return 'about'
