from typing import Generator
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from models.db import Base
from constants import DB_CONNECTION_STRING


if not DB_CONNECTION_STRING:
    raise Exception("DB connection string not providet")

engine = create_engine(DB_CONNECTION_STRING, echo=False, pool_pre_ping=True, pool_recycle=3600) #reconect after 1 hour
session_maker = sessionmaker(bind=engine, expire_on_commit=False)

def create_db() -> None:
    """
    Creates the database tables by calling `Base.metadata.create_all(engine)`.
    """
    Base.metadata.create_all(engine)


def get_db() -> Generator[Session, Any, None]:
    """
    Returns a generator that yields a SQLAlchemy session. This session should be used for all database interactions within the current request context.
    """
    with session_maker() as session:
        yield session
        

def auto_create_db():
    """
    Automatically creates the database if it doesn't already exist.

    This function attempts to connect to the database engine. If an exception is raised, it means the database doesn't exist yet, so it creates the database using the connection string and database name extracted from the `CONNECTION_STRING` variable.

    After creating the database, it calls the `create_db()` function to perform any additional setup or initialization for the database.
    """
    try:
        con = engine.connect()
        create_db()
        con.close()

    except Exception as _:
        connection_string, db_name = DB_CONNECTION_STRING.rsplit("/", 1)

        tmp_engine = create_engine(connection_string)
        with tmp_engine.begin() as session:
            session.exec_driver_sql(f"CREATE DATABASE `{db_name}`")

        create_db()
