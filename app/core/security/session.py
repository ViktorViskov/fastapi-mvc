from datetime import datetime
from datetime import timezone

from fastapi import Request
from fastapi import Response
from fastapi import Depends

from core.config import CONFIG
from services import user_service
from exceptions.scheme import AppException
from models import enums
from models import dto
from core.security import jwt
from core.security import bcrypt_hashing


def get_token(req: Request, res: Response) -> dto.Token:
    session_token = req.cookies.get(CONFIG.COOKIES_KEY_NAME)
    if session_token is None:
        raise AppException(status_code=401, message="Unauthorized")

    token_dict = jwt.decode(session_token)
    if token_dict is None:
        res.delete_cookie(CONFIG.COOKIES_KEY_NAME)
        raise AppException(status_code=401, message="Unauthorized")

    return dto.Token(**token_dict)

def get_user(req: Request, res: Response) -> dto.UserDTO:
    token = get_token(req, res)

    user = user_service.get_by_id(token.user_id)
    if user is None:
        res.delete_cookie(CONFIG.COOKIES_KEY_NAME)
        raise AppException(status_code=401, message="Unauthorized")

    return user

def get_admin(user: dto.UserDTO = Depends(get_user)) -> dto.UserDTO:
    if user.role != enums.UserRole.ADMIN:
        raise AppException(status_code=403, message="Forbidden. Not an admin user")

    return user

async def login(obj: dto.UserLoginDTO, res: Response) -> str:
    NOW = datetime.now(timezone.utc)

    user_db = user_service.get_by_email(obj.email)
    print(obj.password, user_db.password)
    if bcrypt_hashing.validate(obj.password, user_db.password) is False:
        raise AppException("Incorrect password", 401)

    exp_date = NOW + CONFIG.SESSION_TIME
    token = dto.Token(user_id=user_db.id, role=user_db.role)
    token_str = jwt.encode(token.model_dump(), exp_date)

    res.set_cookie(CONFIG.COOKIES_KEY_NAME, token_str, expires=exp_date)
    return token_str

async def logout(res: Response) -> None:
    res.delete_cookie(CONFIG.COOKIES_KEY_NAME)