import os
from pathlib import Path

from dotenv import load_dotenv

from app import create_app
from backend.logging_manager import setup_logging
from backend.search import Search


def main():
    setup_logging()
    es = Search()
    print(es.info())

    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
