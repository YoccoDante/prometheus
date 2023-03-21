# main.py
from flask import Flask
from auth import bpAuth as auth
from flask_cors import CORS



app = Flask(__name__)
app.register_blueprint(auth)
CORS(app)


if __name__ == "__main__":
    app.run()