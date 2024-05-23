from datetime import datetime
from datetime import timezone

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from utils import formating
from utils import validators
from models import db
from models import dto
from services import user_service
from services import token_service


COOKIES_KEY_NAME = "session_token"

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=dto.GetUser)
def register(user: dto.CreateUser):
    
    email = formating.format_string(user.email)
    
    if not email:
        raise HTTPException(
            detail="Email can not be empty",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    
    if not user.password:
        raise HTTPException(
            detail="Password can not be empty",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    
    exist_user = user_service.get_by_email(email)
    if exist_user:
        raise HTTPException(
            detail=f"User '{email}' exist",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    
    return user_service.create(
        user.name,
        user.surname,
        db.User.Role.USER,
        email,
        user.password
    )

@router.post("/login", status_code=status.HTTP_200_OK, response_model=dto.Token)
def login(dto: dto.LoginUser, res: Response):
    email = formating.format_string(dto.email)
    
    user = user_service.get_by_email_and_password(email, dto.password)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
        
    # delete all expired users tokens
    token_service.delete_expired(user.id)
    
    # create session
    token = token_service.create(user.id)
    token_exp_date: datetime = token.expired_at
    res.set_cookie(COOKIES_KEY_NAME, token.hash, expires=token_exp_date.replace(tzinfo=timezone.utc))
    return token

@router.get("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout( req: Request) -> JSONResponse:
    token_hash = req.cookies.get(COOKIES_KEY_NAME)
    
    if token_hash is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    
    token_service.delete_by_hash(token_hash)

@router.get("/validate", response_model=bool)
def check_session( req: Request, res: Response) -> JSONResponse:
    token_hash = req.cookies.get(COOKIES_KEY_NAME, "")
    
    is_valid = validators.validate_token(token_hash)
    if is_valid is False:
        res.delete_cookie(COOKIES_KEY_NAME)
        
    return is_valid
        