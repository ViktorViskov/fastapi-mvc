from models.db import UserDb
from core.db_context import session_maker


def add(user: UserDb)-> UserDb:
    with session_maker.begin() as session:
        session.add(user)
        return user

def update(user: UserDb) -> None:
    with session_maker.begin() as session:
        session.query(UserDb).filter(UserDb.id == user.id).update({
            UserDb.name: user.name,
            UserDb.surname: user.surname,
            UserDb.role: user.role,
            UserDb.email: user.email,
            UserDb.password: user.password
        })

def delete(id: int) -> None:
    with session_maker.begin() as session:
        session.query(UserDb).filter(UserDb.id == id).delete()

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
