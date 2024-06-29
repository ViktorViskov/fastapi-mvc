from datetime import datetime

import jwt

from models import db
from models import dto

  
SECRET_KEY = "SomeRandomSalt"
ALGORITHM = "HS256"

def encode(user_id: int, role: db.User.Role, exp: datetime) -> str:
    token = dto.Token(
        user_id=user_id,
        role=role,
        exp=exp,
    )
    return jwt.encode(token.model_dump(), SECRET_KEY, algorithm=ALGORITHM)
    
def decode(token: str) -> dto.Token | None:
    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return dto.Token(**token_data)
    except jwt.PyJWTError as e:
        # print(e)
        return None
    