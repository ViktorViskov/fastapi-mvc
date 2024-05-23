from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from utils import pages


router = APIRouter(
    prefix="",
    tags=["Pages"],
    default_response_class=HTMLResponse
)

# main pages
@router.get("/")
def main():
    return pages.read_page("main.html")

# auth pages
@router.get("/login")
def login():
    return pages.read_page("login.html")

@router.get("/register")
def register():
    return pages.read_page("register.html")

# panel pages
@router.get("/panel")
def private():
    return pages.read_page("private.html")
