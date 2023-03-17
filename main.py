# main.py
from flask import Flask
from auth import bpAuth as auth


app = Flask(__name__)
app.register_blueprint(auth)


if __name__ == "__main__":
    app.run()