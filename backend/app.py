import os
from logging import DEBUG, basicConfig, error
from pathlib import Path

from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from flask import Flask


def main():
    basicConfig(level=DEBUG)

    dotenv_path = (Path(__file__).parents[1] / ".env").resolve()
    load_dotenv(dotenv_path=dotenv_path)
    username = "elastic"
    password = os.getenv("ELASTIC_PASSWORD")
    elastic_url = os.getenv("ELASTIC_URL")

    client = Elasticsearch(elastic_url, basic_auth=(username, password))
    print(client.info())

    app = Flask(__name__)
    app.run(debug=True)


if __name__ == "__main__":
    main()
