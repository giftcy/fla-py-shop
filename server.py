from shop import Shop
from config import Config

app = Shop(Config)

if __name__ == "__main__":
    app.start().run()
