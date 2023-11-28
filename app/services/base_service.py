from repositories import TokenRepository
from repositories import UserRepository


class BaseService:
    token_repo: TokenRepository
    user_repo: UserRepository
    
    def __init__(self) -> None:
        self.token_repo = TokenRepository()
        self.user_repo = UserRepository()