from os import getenv

from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from models import Base


DEFAULT_LIMIT: int = 1000

class BaseRepository:
    engine: Engine
    session_maker: sessionmaker[Session]
    
    def __init__(self) -> None:
        USER_NAME = getenv("DB_USER")
        USER_PASS = getenv("DB_PASS")
        DB_ADDR = getenv("DB_ADDR")
        DB_PORT = getenv("DB_PORT")
        DB_NAME = getenv("DB_NAME")
        
        connection_string = f"mariadb+pymysql://{USER_NAME}:{USER_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}"
        self.engine = create_engine(connection_string, echo=False)
        self.session_maker = sessionmaker(bind=self.engine, expire_on_commit=False)

    def create_db(self) -> None:
        Base.metadata.create_all(self.engine)