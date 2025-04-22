from fastapi import APIRouter
from fastapi import Query
from fastapi import Path

from models import dto
from services import user_service
from core import dependencies


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/me", response_model=dto.UserDTO)
def get_me(user: dependencies.user_dependency):
    return user

@router.get("/all", response_model=list[dto.UserDTO])
def get_all(limit: int = Query(1000, gt=0), offset: int = Query(0, ge=0)):
    return user_service.get_all(limit, offset)

@router.get("/admin_only", response_model=dto.UserDTO)
def get_admin_only(user: dependencies.admin_dependency):
    return user

@router.get("/{id}", response_model=dto.UserDTO)
def get_by_id(id: int = Path(ge=1)):
    return user_service.get_by_id(id)

@router.get("/email/{email}", response_model=dto.UserDTO)
def get_by_email(email: str):
    return user_service.get_by_email(email)