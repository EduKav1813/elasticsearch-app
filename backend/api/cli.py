from logging import info

from flask.blueprints import Blueprint

from backend.logging_manager import setup_logging
from backend.search import Search

bp = Blueprint("cli", __name__)


@bp.cli.command("reindex")
def reindex():
    """Regenerate the Elasticsearch index."""
    setup_logging()
    response = Search().reindex()
    info(
        f'Index with {len(response["items"])} documents created '
        f'in {response["took"]} milliseconds.'
    )
