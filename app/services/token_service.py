from datetime import datetime

from models import db
from .base_service import BaseService


class TokenService(BaseService):        
    def get_by_id(self, id: int) -> db.Token | None:
        return self.token_repo.get_by_id(id)
        
    def get_by_user_id(self, user_id: int) -> list[db.Token]:
        return self.token_repo.get_by_user_id(user_id)
    
    def get_by_hash(self, hash: str) -> db.Token | None:
        return self.token_repo.get_by_hash(hash)
        
    def create(self, user: db.User, hash: str, valid_to: datetime) -> db.Token:
        token = db.Token()
        token.user_id = user.id
        token.hash = hash
        token.expired_at = valid_to
        
        token_id = self.token_repo.add(token)
        return self.get_by_id(token_id)
        
    def delete(self, token: db.Token) -> None:
        self.token_repo.delete(token.id)
        
    def delete_expired(self, tokens: list[db.Token]) -> None:
        now = datetime.utcnow()
        for t in tokens:
            if t.expired_at < now:
                self.delete(t)
        
    