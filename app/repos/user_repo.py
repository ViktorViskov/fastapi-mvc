from sqlalchemy import Delete
from sqlalchemy import Update
from sqlalchemy.sql.functions import current_timestamp

from models.db import UserDb
from utils.db_context import session_maker


def add(name: str, surname: str, role: UserDb.Role, email: str, password: str)-> UserDb:
    with session_maker.begin() as session:
        user = UserDb()
        user.name = name
        user.surname = surname
        user.role = role
        user.email = email
        user.password = password

        session.add(user)
        session.flush()

        return user

def update(id: int, name: str, surname: str, role: UserDb.Role, email: str, password: str) -> None:
    with session_maker.begin() as session:
        session.execute(Update(UserDb).where(UserDb.id == id).values({
            UserDb.name: name,
            UserDb.surname: surname,
            UserDb.role: role,
            UserDb.email: email,
            UserDb.password: password,
            UserDb.updated_at: current_timestamp()
        }))

def delete(id: int) -> None:
    with session_maker.begin() as session:
        session.execute(Delete(UserDb).where(UserDb.id == id))
    
def get(limit:int = 1000, offset: int = 0) -> list[UserDb]:
    with session_maker() as session:
        return session.query(UserDb).limit(limit).offset(offset).all()

def get_by_id(id: int) -> UserDb | None:
    with session_maker() as session:
        return session.query(UserDb).where(
            UserDb.id == id          
        ).first()

def get_by_email(email: str) -> UserDb | None:
    with session_maker.begin() as session:
        return session.query(UserDb).where(
            UserDb.email == email          
        ).first()
