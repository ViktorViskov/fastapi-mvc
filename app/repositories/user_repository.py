from datetime import datetime
from os import getenv
from random import randint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.functions import random

from models import db
from .base_repository import BaseRepository
from .base_repository import DEFAULT_LIMIT


class UserRepository(BaseRepository):

    def add(self, obj: db.User) -> int:
        with self.session_maker.begin() as session:

            session.add(obj)
            session.flush()

            return obj.id


    def update(self, obj: db.User) -> None:
        with self.session_maker.begin() as session:
            to_update = session.query(db.User).where(
                db.User.id == obj.id          
            ).first()

            if to_update:
                to_update.name = obj.name
                to_update.surname = obj.surname
                to_update.role = obj.role
                to_update.email = obj.email
                to_update.password = obj.password
                to_update.updated_at = current_timestamp()

    def delete(self, obj_id: int) -> None:
        with self.session_maker.begin() as session:
            
            to_delete = session.query(db.User).where(
                db.User.id == obj_id         
            ).first()
            
            if to_delete:
                session.delete(to_delete)
        
    def get(self, limit:int = DEFAULT_LIMIT, offset: int = 0) -> list[db.User]:
        with self.session_maker.begin() as session:
            objs = session.query(db.User).limit(limit).offset(offset).all()
            
            return objs

    def get_by_id(self, obj_id: int) -> db.User | None:
        with self.session_maker.begin() as session:
            item = session.query(db.User).where(
                db.User.id == obj_id          
            ).first()

            return item

    def get_by_email(self, email: str) -> db.User | None:
        with self.session_maker.begin() as session:
            item = session.query(db.User).where(
                db.User.email == email          
            ).first()

            return item
