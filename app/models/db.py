from enum import StrEnum

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
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
    
    class Role(StrEnum):
        ADMIN = "admin"
        USER = "user"
        GUEST = "guest"

# one to one relationship
class TaxAccount(Base):
    __tablename__ = 'tax_accounts'
    id = Column("id", Integer, ForeignKey("users.id"), index=True, primary_key=True)
    rate = Column("rate", Float(precision=2))
    updated_at = Column("updated_at", DateTime(), default=current_timestamp())
    created_at = Column("created_at", DateTime(), default=current_timestamp())

# one to many relationship
class Salary(Base):
    __tablename__ = 'salaries'
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    user_id = Column("user_id", Integer(), ForeignKey('users.id'))
    amount = Column("amount", Float(precision=2))
    amount_hours = Column("amount_hours", Float(precision=1))
    salary_date = Column("salary_date", DateTime())
    updated_at = Column("updated_at", DateTime(), default=current_timestamp())
    created_at = Column("created_at", DateTime(), default=current_timestamp())