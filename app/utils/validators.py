from datetime import datetime
from datetime import timezone

from services import token_service


def validate_token(token_hash: str) -> bool:      
    now =  datetime.now(timezone.utc).replace(tzinfo=None)
    
    token = token_service.get_by_hash(token_hash)
    if not token:
        return False
        
    # delete expired token
    if token and token.expired_at < now:
        token_service.delete(token.id)
        return False

    return True