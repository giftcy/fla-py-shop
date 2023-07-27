from flask import Flask

from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()






class Shop():
    # app = Flask(__name__)
    def __init__(self, config_class=''):
        
        self.config_class = config_class

        self.start()
        
    def start(self):
        self.app = Flask(__name__)
        self.app.config.from_object(self.config_class)

        # importing routes for the app
        from .main import main as mb
        self.app.register_blueprint(mb)

        from .auth import auth as ab
        self.app.register_blueprint(ab,url_prefix='/auth')

        #initializing flask extensions
        bootstrap.init_app(self.app)
        mail.init_app(self.app)
        db.init_app(self.app)
        moment.init_app(self.app)

        return self.app

