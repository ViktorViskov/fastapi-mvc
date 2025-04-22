from fastapi import APIRouter
from fastapi import status
from fastapi import Response

from models import dto
from services import user_service
from core.security import session
from core import dependencies


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=dto.UserDTO)
async def register(user: dto.UserCreateDTO):
    return user_service.create_user(user)

@router.post("/login", status_code=status.HTTP_200_OK, response_model=str)
async def login(obj: dto.UserLoginDTO, res: Response):
    return await session.login(obj, res)

@router.get("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(res: Response):
    await session.logout(res)

@router.get("/validate", response_model=dto.Token)
async def check_session(token: dependencies.token_dependency):
    return token

@router.put("/password/update", status_code=204)
def update_password(dto: dto.UserUpdatePassDTO, user: dependencies.user_dependency):
    user_service.update_password(user, dto)

@router.post("/password/reset", status_code=204)
def reset_password(email: str):
    user_service.reset_password(email)