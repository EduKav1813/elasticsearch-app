from logging import debug

from backend.searchengine import search_engine
from flask import jsonify, request
from flask.blueprints import Blueprint
from flask_cors import cross_origin

bp = Blueprint("search", __name__)


@bp.post("/")
@cross_origin
def get_quotes():
    query = request.form.get("query", "")
    debug(f"Search for quotes with query: '{query}'")
    results = search_engine.search(
        query={"multi_match": {"query": query, "fields": ["quote", "author"]}},
        size=5,
    )

    num_quotes = len(results["hits"]["hits"])
    quotes_list = []
    if num_quotes > 0:
        debug(f"Found {num_quotes} quotes:")

        for index, result in enumerate(results["hits"]["hits"], start=1):
            quote = result["_source"]["quote"]
            author = result["_source"]["author"]
            quotes_list.append({"quote": quote, "author": author})
            debug(f"#{index}. {quote} {author}")

    else:
        debug("Found no results\n")

    return jsonify(quotes_list)
