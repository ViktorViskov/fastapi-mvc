from fastapi import APIRouter
from fastapi import Query
from fastapi import Path
from fastapi import HTTPException

from models import db
from models import dto
from services import user_service
from utils import dependencies


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/me", response_model=dto.GetUser)
def get_me(user: dependencies.user_dependency) -> db.User:
    return user

@router.get("/all", response_model=list[dto.GetUser])
def get_all(limit: int = Query(1000, gt=0), offset: int = Query(0, ge=0)) -> list[db.User]:
    return user_service.get(limit, offset)

@router.get("/{id}", response_model=dto.GetUser)
def get_by_id(id: int = Path(ge=1)) -> db.User | None:
    user = user_service.get_by_id(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.get("/email/{email}", response_model=dto.GetUser)
def get_by_email(email: str) -> db.User | None:
    user = user_service.get_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user    