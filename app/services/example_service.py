from datetime import datetime

from models import db
from repositories import TokenRepository
from .base_service import BaseService


class ExampleService(BaseService):
    primary_repo: TokenRepository
    
    def __init__(self) -> None:
        super().__init__()
        self.primary_repo = self.token_repo