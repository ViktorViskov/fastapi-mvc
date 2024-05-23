from datetime import datetime
from datetime import timezone
from hashlib import sha256
from os import getenv
from random import randint


HASH_SALT = getenv("HASH_SALT", "")

def hash_password(password: str) -> str:
    to_hash = password + HASH_SALT
    return sha256(to_hash.encode()).hexdigest()

def generate_hash() -> str:
    datetime_now = datetime.now(timezone.utc).replace(tzinfo=None)
    timestamp = datetime_now.timestamp()
    random_number = randint(0, 999999)
    to_hash = f"{datetime_now} {timestamp} {random_number} {HASH_SALT}"
    return sha256(to_hash.encode()).hexdigest()