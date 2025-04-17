from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from os import getenv


def _get_from_env(var_name: str) -> str:
    value = getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' must be set.")
    return value

@dataclass(frozen=True)
class Config:
    DB_CONNECTION_STRING: str
    COOKIES_KEY_NAME: str
    SESSION_TIME: timedelta
    HASH_SALT: str

    @staticmethod
    def get_config() -> Config:
        db_connection_string = getenv("DB_CONNECTION_STRING", "sqlite:///db.sqlite")
        if db_connection_string == "":
            raise ValueError(
                "Environment variable 'DB_CONNECTION_STRING' must be set and cannot be empty. "
            )

        cookies_key_name = "session_token"
        session_time = timedelta(days=30)
        hash_salt = getenv("HASH_SALT", "SomeRandomStringHere")

        return Config(db_connection_string, cookies_key_name, session_time, hash_salt)


CONFIG = Config.get_config()
