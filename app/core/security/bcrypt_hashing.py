from time import time
from random import randint

from passlib.context import CryptContext
from core.config import CONFIG


CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str) -> str:
    to_hash = password + CONFIG.HASH_SALT
    return CONTEXT.hash(to_hash)

def validate(plain_password: str, hashed_password: str) -> bool:
    try:
        to_verify = plain_password + CONFIG.HASH_SALT
        return CONTEXT.verify(to_verify, hashed_password)
    except Exception as e:
        print(e)
        return False

def random_hash() -> str:
    timestamp = time()
    random_number = randint(0, 999999)
    return CONTEXT.hash(f"{timestamp} {random_number} {CONFIG.HASH_SALT}")

