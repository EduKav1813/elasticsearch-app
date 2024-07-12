from backend.searchengine import search_engine
from flask.blueprints import Blueprint
from flask import request, jsonify

bp = Blueprint("search", __name__)


@bp.get("/")
def get_quotes():
    query = request.form.get("query", "")
    results = search_engine.search(
        query={"multi_match": {"query": query, "fields": ["quote", "author"]}},
        size=5,
    )

    print(results)
    return jsonify(results["hits"]["hits"])
