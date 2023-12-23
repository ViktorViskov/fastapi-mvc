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
        self.engine = create_engine(getenv("DB_CONNECTION_STRING"), echo=False, pool_pre_ping=True, pool_recycle=3600) #reconect after 1 hour
        self.session_maker = sessionmaker(bind=self.engine, expire_on_commit=False)

    def create_db(self) -> None:
        Base.metadata.create_all(self.engine)