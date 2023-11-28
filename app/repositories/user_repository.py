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
        Session = sessionmaker(bind=self.engine)
        session = Session()

        session.add(obj)
        session.flush()

        item_id = obj.id

        session.commit()
        session.close()

        return item_id

    def update(self, obj: db.User) -> None:
        Session = sessionmaker(bind=self.engine)
        session = Session()

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

            session.commit()

        session.close()

    def delete(self, obj_id: int) -> None:
        Session = sessionmaker(bind=self.engine)
        session = Session()

        to_delete = session.query(db.User).where(
            db.User.id == obj_id         
        ).first()
        
        if to_delete:
            session.delete(to_delete)
            session.commit()

        session.close()
        
    def get(self, limit:int = DEFAULT_LIMIT, offset: int = 0) -> list[db.User]:
        Session = sessionmaker(bind=self.engine)
        session = Session()

        objs = session.query(db.User).limit(limit).offset(offset).all()

        session.close()
        return objs

    def get_by_id(self, obj_id: int) -> db.User | None:
        Session = sessionmaker(bind=self.engine)
        session = Session()

        item = session.query(db.User).where(
            db.User.id == obj_id          
        ).first()

        session.close()

        return item

    def get_by_email(self, email: str) -> db.User | None:
        Session = sessionmaker(bind=self.engine)
        session = Session()

        item = session.query(db.User).where(
            db.User.email == email          
        ).first()

        session.close()

        return item
