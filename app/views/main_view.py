from datetime import datetime

from fastapi.requests import Request
from models.dto import UserDTO
from core.templates import templates


def main_page(req: Request):
    now = datetime.now()
    return templates.TemplateResponse(
        req, "main.jinja", {"date": now.replace(microsecond=0)}
    )

def auth_page(req: Request, user: UserDTO):
    return templates.TemplateResponse(
        req, "auth.jinja", {"user": user}
    )