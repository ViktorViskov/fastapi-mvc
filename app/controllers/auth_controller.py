from datetime import datetime
from datetime import timezone

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi.requests import Request

from utils import formating
from models import db
from models import dto
from services import user_service
from services import jwt_service
from utils.bcrypt_hashing import HashLib
from utils import dependencies
from utils.config import CONFIG


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=dto.GetUser)
async def register(user: dto.CreateUser):
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
        db.UserDb.Role.USER,
        email,
        user.password
    )

@router.post("/login", status_code=status.HTTP_200_OK, response_model=str)
async def login(obj: dto.LoginUser, res: Response):
    NOW = datetime.now(timezone.utc)
    
    email = formating.format_string(obj.email)
    
    user = user_service.get_by_email(email)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    
    if HashLib.validate(obj.password, user.password) is False:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect password")
    
    exp_date = NOW + CONFIG.SESSION_TIME
    token = dto.Token(user_id=user.id, role=user.role) 
    token_str = jwt_service.encode(token.model_dump(), exp_date)
    
    res.set_cookie(CONFIG.COOKIES_KEY_NAME, token_str, expires=exp_date)
    return token_str

@router.get("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(res: Response):
    res.delete_cookie(CONFIG.COOKIES_KEY_NAME)

@router.get("/validate", response_model=dto.Token)
async def check_session( req: Request, res: Response):
    token = req.cookies.get(CONFIG.COOKIES_KEY_NAME, "")
    
    data = jwt_service.decode(token)
    if data is None:
        res.delete_cookie(CONFIG.COOKIES_KEY_NAME)
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token is invalid")
        
    return data

@router.put("/password/update", status_code=204)
def update_password(dto: dto.UpdateUserPass, user: dependencies.user_dependency):    
    if dto.old_password == dto.new_password:
        raise HTTPException(status_code=422, detail="Passwords can not be same")
    
    if HashLib.validate(dto.old_password, user.password) is False:
        raise HTTPException(status_code=401, detail="Current password is incorrect")
    
    user_service.update_password(user.id, dto.new_password)
    
@router.post("/password/reset", status_code=204)
def reset_password(email: str):
    user = user_service.get_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    new_pass = user_service.reset_password(user.id)
    print(f"User {user.email} new password: {new_pass}")