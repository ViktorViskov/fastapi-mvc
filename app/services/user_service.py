from random import randint

from models import db
from models import dto
from repos import user_repo

from utils.bcrypt_hashing import HashLib
from utils import formating
from mappers import user_mapper


def get(limit: int, offset: int) -> list[db.UserDb]:
    return user_repo.get(limit=limit, offset=offset)
            
def get_by_id(id: int) -> db.UserDb | None:
    return user_repo.get_by_id(id)
    
def get_by_email(email: str) -> db.UserDb | None:
    return user_repo.get_by_email(email.lower().strip())

def create(name: str, surname: str, role: db.UserDb.Role, email: str, password: str) -> dto.GetUser:
    name = formating.format_string(name)
    surname = formating.format_string(surname)
    email = formating.format_string(email)
    pass_hash = HashLib.hash(password)
    user = user_repo.add(name, surname, role, email, pass_hash)
    return user_mapper.db_to_get_dto(user)

def update(id: int, name: str, surname: str, role: db.UserDb.Role, email: str, password: str) -> None:
    name = formating.format_string(name)
    surname = formating.format_string(surname)
    email = formating.format_string(email)
    pass_hash = HashLib.hash(password)
    user_repo.update(id ,name, surname, role, email, pass_hash)
    
def update_name_surname(id: int, name: str, surname: str) -> None:
    user = get_by_id(id)
    if user is None:
        return
    
    name = formating.format_string(name)
    surname = formating.format_string(surname)
    user_repo.update(
        user.id,
        name,
        surname,
        user.role,
        user.email,
        user.password
    )

def update_password(id: int, new_password: str) -> None:
    user = get_by_id(id)
    if user is None:
        return
    
    new_pass_hash = HashLib.hash(new_password)
    user_repo.update(
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
        return ""
    
    new_password = str(randint(100000, 999999))
    pass_hash = HashLib.hash(new_password)
    user_repo.update(
        user.id,
        user.name,
        user.surname,
        user.role,
        user.email,
        pass_hash
    )
    
    return new_password
    
def delete(id: int) -> None:
    user_repo.delete(id)
    
    