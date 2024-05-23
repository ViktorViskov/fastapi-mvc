from random import randint

from models import db
from repositories import user_repository
from repositories import token_repository

from utils import hashing
from utils import formating


def get(limit: int, offset: int) -> list[db.User]:
    return user_repository.get(limit=limit, offset=offset)
            
def get_by_id(id: int) -> db.User | None:
    return user_repository.get_by_id(id)
    
def get_by_email(email: str) -> db.User | None:
    return user_repository.get_by_email(email.lower().strip())

def get_by_email_and_password(email: str, password: str) -> db.User | None:
    result = None
    
    pass_hash = hashing.hash_password(password)
    user = user_repository.get_by_email(email)
    if user and user.password == pass_hash:
        result = user
    
    return result

def get_by_token_hash(hash: str) -> db.User:
    token = token_repository.get_by_hash(hash)
    if token is None:
        return None
    
    return user_repository.get_by_id(token.user_id)

def create(name: str, surname: str, role: db.User.Role, email: str, password: str) -> db.User:
    name = formating.format_string(name)
    surname = formating.format_string(surname)
    email = formating.format_string(email)
    pass_hash = hashing.hash_password(password)
    return user_repository.add(name, surname, role, email, pass_hash)

def update(id: int, name: str, surname: str, role: db.User.Role, email: str, password: str) -> None:
    name = formating.format_string(name)
    surname = formating.format_string(surname)
    email = formating.format_string(email)
    pass_hash = hashing.hash_password(password)
    user_repository.update(id ,name, surname, role, email, pass_hash)
    
def update_name_surname(id: int, name: str, surname: str) -> None:
    user = get_by_id(id)
    if user is None:
        return
    
    name = formating.format_string(name)
    surname = formating.format_string(surname)
    user_repository.update(
        user.id,
        name,
        surname,
        user.role,
        user.email,
        user.password
    )

def update_password(id: int, old_password: str, new_password: str) -> None:
    user = get_by_id(id)
    if user is None:
        return
    
    old_pass_hash = hashing.hash_password(old_password)
    if user.password != old_pass_hash:
        return
    
    new_pass_hash = hashing.hash_password(new_password)
    user_repository.update(
        user.id,
        user.name,
        user.surname,
        user.role,
        user.email,
        new_pass_hash
    )

def reset_password(id: int) -> str:    
    user = get_by_id(id)
    if user is None:
        return
    
    new_password = str(randint(100000, 999999))
    pass_hash = hashing.hash_password(new_password)
    user_repository.update(
        user.id,
        user.name,
        user.surname,
        user.role,
        user.email,
        pass_hash
    )
    
    return new_password
    
def delete(id: int) -> None:
    user_repository.delete(id)
    
    