from flask import Flask

from backend.api import cli, search


def create_app():
    app = Flask(__name__)
    app.register_blueprint(cli.bp)
    app.register_blueprint(search.bp)
    return app


app = create_app()
