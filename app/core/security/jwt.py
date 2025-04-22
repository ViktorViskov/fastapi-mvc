from datetime import datetime
from datetime import timezone
import jwt


SECRET_KEY = "SomeRandomSalt"
ALGORITHM = "HS256"


def encode(data: dict, exp: datetime) -> str:
    iat = datetime.now(timezone.utc).replace(tzinfo=None)
            
    token_data = {
        "iat": iat,
        "exp": exp,
        "body": data
    }
    
    return jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

def decode(token: str) -> dict | None:
    try:
        data:dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return data.get("body")
    except jwt.PyJWTError as e:
        print(e)
        return None
