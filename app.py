from flask import Flask
from config import Config
from routes import setup_routes

app = Flask(__name__)
app.config.from_object(Config)
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
