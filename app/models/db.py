from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql.functions import current_timestamp

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    name = Column("name", String(32))
    surname = Column("surname", String(32))
    role = Column("role", String(32))
    email = Column("email", String(256), unique=True)
    password = Column("password", String(256))
    updated_at = Column("updated_at", DateTime(), default=current_timestamp())
    created_at = Column("created_at", DateTime(), default=current_timestamp())

class Token(Base):
    __tablename__ = 'tokens'
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    user_id = Column("user_id", Integer(), ForeignKey('users.id'))
    hash = Column("hash", String(256), unique=True)
    expired_at = Column("expired_at", DateTime())
    created_at = Column("created_at", DateTime(), default=current_timestamp())