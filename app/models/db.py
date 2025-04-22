from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Enum
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

from models import enums


Base = declarative_base()

class UserDb(Base):
    __tablename__ = 'users'
    id = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    name = mapped_column("name", String)
    surname = mapped_column("surname", String)
    role = mapped_column("role", Enum(enums.UserRole), default=enums.UserRole.USER)
    email = mapped_column("email", String, unique=True)
    password = mapped_column("password", String)
    updated_at = mapped_column("updated_at", DateTime(), server_default=current_timestamp(), server_onupdate=current_timestamp())
    created_at = mapped_column("created_at", DateTime(), server_default=current_timestamp())

# one to one relationship
class TaxAccountDb(Base):
    __tablename__ = 'tax_accounts'
    id = mapped_column("id", Integer, ForeignKey("users.id"), index=True, primary_key=True)
    rate = mapped_column("rate", Float(precision=2))
    updated_at = mapped_column("updated_at", DateTime(), server_default=current_timestamp(), server_onupdate=current_timestamp())
    created_at = mapped_column("created_at", DateTime(), server_default=current_timestamp())

# one to many relationship
class SalaryDb(Base):
    __tablename__ = 'salaries'
    id = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    user_id = mapped_column("user_id", Integer(), ForeignKey('users.id'))
    amount = mapped_column("amount", Float(precision=2))
    amount_hours = mapped_column("amount_hours", Float(precision=1))
    salary_date = mapped_column("salary_date", DateTime())
    updated_at = mapped_column("updated_at", DateTime(), server_default=current_timestamp(), server_onupdate=current_timestamp())
    created_at = mapped_column("created_at", DateTime(), server_default=current_timestamp())