from flask import Flask





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



        return self.app

