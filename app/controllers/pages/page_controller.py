from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from views import main_view
from core.dependencies import user_dependency

router = APIRouter(
    prefix="",
    tags=["Pages"],
    default_response_class=HTMLResponse
)

@router.get("/")
def main(req: Request):
    return main_view.main_page(req)

@router.get("/check")
def check(req: Request, user: user_dependency):
    return main_view.auth_page(req, user)
