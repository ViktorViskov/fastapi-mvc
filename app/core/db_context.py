
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.db import Base
from core.config import CONFIG


engine = create_engine(CONFIG.DB_CONNECTION_STRING, echo=False, pool_pre_ping=True, pool_recycle=3600) #reconect after 1 hour
session_maker = sessionmaker(bind=engine, expire_on_commit=False)

def create_tables() -> None:
    """
    Creates the database tables by calling `Base.metadata.create_all(engine)`.
    """
    Base.metadata.create_all(engine)

def auto_create_db():
    """
    Automatically creates the database if it doesn't already exist.

    This function attempts to connect to the database engine. If an exception is raised, it means the database doesn't exist yet, so it creates the database using the connection string and database name extracted from the `CONNECTION_STRING` variable.

    After creating the database, it calls the `create_db()` function to perform any additional setup or initialization for the database.
    """
    try:
        con = engine.connect()
        create_tables()
        con.close()

    except Exception as _:
        connection_string, db_name = CONFIG.DB_CONNECTION_STRING.rsplit("/", 1)

        tmp_engine = create_engine(connection_string)
        with tmp_engine.begin() as session:
            session.exec_driver_sql(f"CREATE DATABASE `{db_name}`")

        create_tables()
