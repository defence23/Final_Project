import os

from dotenv import load_dotenv

load_dotenv()


def get_env_or_raise(key: str) -> str:
    """Get an environment variable or raise an exception."""
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} is not set")
    return value


DATABASE_URL = get_env_or_raise("DATABASE_URL")
