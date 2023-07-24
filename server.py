from shop import Shop
from config import config

app = Shop(config['default'])

if __name__ == "__main__":
    app.start().run()
