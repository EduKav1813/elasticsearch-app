from logging import info

from backend.logging_manager import setup_logging
from backend.searchengine import search_engine
from flask.blueprints import Blueprint

bp = Blueprint("cli", __name__)


@bp.cli.command("reindex")
def reindex():
    """Regenerate the Elasticsearch index."""
    setup_logging()
    response = search_engine.reindex()
    info(
        f'Index with {len(response["items"])} documents created '
        f'in {response["took"]} milliseconds.'
    )
