from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.functions import random

from models import db
from .base_repository import BaseRepository
from .base_repository import DEFAULT_LIMIT


Item = db.Token

class TokenRepository(BaseRepository):

    def add(self, obj: Item) -> int | None:
        with self.session_maker.begin() as session:

            session.add(obj)
            session.flush()
            
            return obj.id

    def delete(self, obj_id: int) -> None:
        with self.session_maker.begin() as session:
            to_delete = session.query(Item).where(
                Item.id == obj_id         
            ).first()
            
            if to_delete:
                session.delete(to_delete)

    def get_by_id(self, obj_id: int) -> Item | None:
        with self.session_maker.begin() as session:
            item = session.query(Item).where(
                Item.id == obj_id          
            ).first()
            
            return item
    
    def get_by_user_id(self, user_id: int, limit: int = DEFAULT_LIMIT, offset: int = 0) -> list[Item]:
        with self.session_maker.begin() as session:
            objs = session.query(Item).where(
                Item.user_id == user_id
            ).limit(limit).offset(offset).all()

            return objs
    
    def get_by_hash(self, obj_hash: str) -> Item | None:
        with self.session_maker.begin() as session:

            item = session.query(Item).where(
                Item.hash == obj_hash          
            ).first()

            return item
