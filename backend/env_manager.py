import os
from logging import info, warning
from pathlib import Path

import pydantic
from backend.logging_manager import setup_logging
from dotenv import load_dotenv

setup_logging()


def setup_env():
    if not pydantic.TypeAdapter(bool).validate_python(
        os.environ.get("USE_ENV", "True")
    ):
        info(f"USE_ENV is set to False. Abort loading .env")
        return

    env_path = Path(__file__).parents[1] / ".env"
    info(f"Load .env configuration from '{env_path}'")
    is_set = load_dotenv(env_path, verbose=True)
    if not is_set:
        warning(
            "No environment variables set. Possibly the .env file is empty or path to file is incorrect"
        )
    else:
        info("Loaded .env")
