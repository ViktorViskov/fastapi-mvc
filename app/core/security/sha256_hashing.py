from time import time
from hashlib import sha256
from random import randint

from core.config import CONFIG


class HashLib:
    @staticmethod
    def hash(password: str) -> str:
        to_hash = password + CONFIG.HASH_SALT
        return sha256(to_hash.encode()).hexdigest()

    @staticmethod
    def validate(plain_password: str, hashed_password: str) -> bool:
        return hash(plain_password) == hashed_password

    @staticmethod
    def random_hash() -> str:
        random_number = randint(0, 999999)
        timestamp = time()
        to_hash = f"{timestamp} {random_number} {CONFIG.HASH_SALT}"
        return sha256(to_hash.encode()).hexdigest()