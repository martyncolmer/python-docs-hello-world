from flask import Flask
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def hello():
        return "Hello  Mr " + os.getenv('DBONE', "Not Found")

    return app