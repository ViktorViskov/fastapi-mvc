from datetime import datetime
from hashlib import sha256
from os import getenv
from random import randint


HASH_SALT = getenv("HASH_SALT", "")

class HashHandler:
    def hash_password(self, password: str) -> str:
        to_hash = password + HASH_SALT
        return sha256(to_hash.encode()).hexdigest()
    
    def generate_hash(self) -> str:
        datetime_now = datetime.utcnow()
        timestamp = datetime_now.timestamp()
        random_number = randint(0, 999999)
        to_hash = f"{datetime_now} {timestamp} {random_number} {HASH_SALT}"
        return sha256(to_hash.encode()).hexdigest()