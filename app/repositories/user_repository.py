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


Item = db.User

class UserRepository(BaseRepository):

    def add(self, obj: Item) -> int:
        with self.session_maker.begin() as session:

            session.add(obj)
            session.flush()

            return obj.id


    def update(self, obj: Item) -> None:
        with self.session_maker.begin() as session:
            to_update = session.query(Item).where(
                Item.id == obj.id          
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
            
            to_delete = session.query(Item).where(
                Item.id == obj_id         
            ).first()
            
            if to_delete:
                session.delete(to_delete)
        
    def get(self, limit:int = DEFAULT_LIMIT, offset: int = 0) -> list[Item]:
        with self.session_maker.begin() as session:
            objs = session.query(Item).limit(limit).offset(offset).all()
            
            return objs

    def get_by_id(self, obj_id: int) -> Item | None:
        with self.session_maker.begin() as session:
            item = session.query(Item).where(
                Item.id == obj_id          
            ).first()

            return item

    def get_by_email(self, email: str) -> Item | None:
        with self.session_maker.begin() as session:
            item = session.query(Item).where(
                Item.email == email          
            ).first()

            return item
