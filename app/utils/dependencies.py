from typing import Annotated

from fastapi import Depends
from fastapi import Request
from fastapi import Response
from fastapi import HTTPException

from constants import COOKIES_KEY_NAME
from models import db
from services import user_service
from services import jwt_service


def get_user(req: Request, res: Response) -> db.User:
    session_token = req.cookies.get(COOKIES_KEY_NAME)
    if session_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    token = jwt_service.decode(session_token)
    if token is None:
        res.delete_cookie(COOKIES_KEY_NAME)
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    user = user_service.get_by_id(token.user_id)
    if user is None:
        res.delete_cookie(COOKIES_KEY_NAME)
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return user

user_dependency = Annotated[db.User, Depends(get_user)]