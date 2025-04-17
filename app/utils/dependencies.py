from typing import Annotated

from fastapi import Depends
from fastapi import Request
from fastapi import Response
from fastapi import HTTPException

from utils.config import CONFIG
from models import db
from models import dto
from services import user_service
from services import jwt_service


def get_user(req: Request, res: Response) -> db.UserDb:
    session_token = req.cookies.get(CONFIG.COOKIES_KEY_NAME)
    if session_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    token_dict = jwt_service.decode(session_token)
    if token_dict is None:
        res.delete_cookie(CONFIG.COOKIES_KEY_NAME)
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    token = dto.Token(**token_dict)
    
    user = user_service.get_by_id(token.user_id)
    if user is None:
        res.delete_cookie(CONFIG.COOKIES_KEY_NAME)
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return user

def get_admin(user: db.UserDb = Depends(get_user)) -> db.UserDb:
    if user.role != db.UserDb.Role.ADMIN:
        raise HTTPException(status_code=403, detail="Forbidden. Not an admin user")
    
    return user

user_dependency = Annotated[db.UserDb, Depends(get_user)]
admin_dependency = Annotated[db.UserDb, Depends(get_admin)]