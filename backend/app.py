from flask import Flask

from backend.api import cli


def create_app():
    app = Flask(__name__)
    app.register_blueprint(cli.bp)
    return app


app = create_app()
