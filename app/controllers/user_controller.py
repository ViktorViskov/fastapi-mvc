from fastapi import APIRouter
from fastapi import Query
from fastapi import Path
from fastapi import HTTPException

from models import db
from models import dto
from services import user_service
from utils import hashing


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/", response_model=list[dto.GetUser])
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

@router.get("/token/{hash}", response_model=dto.GetUser)
def get_by_token_hash(hash: str) -> db.User | None:
    user = user_service.get_by_token_hash(hash)      
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.delete("/{id}", status_code=204)
def delete(id: int = Path(ge=1)):    
    user = user_service.get_by_id(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_service.delete(user.id)

@router.put("/{id}", status_code=204)
def update(dto: dto.UpdateUser, id: int = Path(ge=1)):
    user = user_service.get_by_id(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_service.update_name_surname(user.id, dto.name, dto.surname)

@router.put("/password/{id}", status_code=204)
def update_password(dto: dto.UpdateUserPass, id: int = Path(ge=1)):
    user = user_service.get_by_id(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not dto.old_password or not dto.new_password:
        raise HTTPException(status_code=422, detail="Password can not be empty")
    
    if dto.old_password == dto.new_password:
        raise HTTPException(status_code=422, detail="Passwords can not be same")
    
    old_password = hashing.hash_password(dto.old_password)
    if user.password != old_password:
        raise HTTPException(status_code=401, detail="Incorrect old password")
    
    user_service.update_password(user.id, dto.old_password, dto.new_password)
    
@router.post("/password/reset/{id}", status_code=204)
def reset_password(dto: dto.ResetUserPass):
    user = user_service.get_by_email(dto.email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    new_pass = user_service.reset_password(user.id)
    print(new_pass)