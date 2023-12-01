from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.functions import random

from models import db
from .base_repository import BaseRepository
from .base_repository import DEFAULT_LIMIT


class TokenRepository(BaseRepository):

    def add(self, obj: db.Token) -> int | None:
        with self.session_maker.begin() as session:

            session.add(obj)
            session.flush()
            
            return obj.id

    def delete(self, obj_id: int) -> None:
        with self.session_maker.begin() as session:
            to_delete = session.query(db.Token).where(
                db.Token.id == obj_id         
            ).first()
            
            if to_delete:
                session.delete(to_delete)

    def get_by_id(self, obj_id: int) -> db.Token | None:
        with self.session_maker.begin() as session:
            item = session.query(db.Token).where(
                db.Token.id == obj_id          
            ).first()
            
            return item
    
    def get_by_user_id(self, user_id: int, limit: int = DEFAULT_LIMIT, offset: int = 0) -> list[db.Token]:
        with self.session_maker.begin() as session:
            objs = session.query(db.Token).where(
                db.Token.user_id == user_id
            ).limit(limit).offset(offset).all()

            return objs
    
    def get_by_hash(self, obj_hash: str) -> db.Token | None:
        with self.session_maker.begin() as session:

            item = session.query(db.Token).where(
                db.Token.hash == obj_hash          
            ).first()

            return item
