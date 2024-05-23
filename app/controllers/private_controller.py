from fastapi import APIRouter

from models import dto
from utils import dependencies
from utils import pages


router = APIRouter(
    prefix="/private",
    tags=["Private"]
)

@router.get("/api", response_model=dto.GetUser)
def get_api(user: dependencies.user_dependency):
    return user

@router.get("/page", response_model=dto.GetUser)
def get_page(user: dependencies.user_dependency):    
    return pages.read_page("private.html")
