from typing import Annotated

from fastapi import Depends
from fastapi import Request
from fastapi import Response
from fastapi import HTTPException

from controllers.auth_controller import COOKIES_KEY_NAME
from models.db import User
from services import user_service
from utils import validators


def get_user(req: Request, res: Response) -> str:
    session_token = req.cookies.get(COOKIES_KEY_NAME)
    if session_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    if validators.validate_token(session_token) is False:
        res.delete_cookie(COOKIES_KEY_NAME)
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return user_service.get_by_token_hash(session_token)

user_dependency = Annotated[User, Depends(get_user)]