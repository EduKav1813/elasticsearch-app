from backend.api import cli, search
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.register_blueprint(cli.bp)
    app.register_blueprint(search.bp)

    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config["CORS_HEADERS"] = "Content-Type"

    return app


app = create_app()
