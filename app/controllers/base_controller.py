from dataclasses import asdict

from fastapi.responses import JSONResponse

from models import dto
from services import UserService
from services import TokenService
from utils import HashHandler
from utils import FormatHandler


class BaseController:
    user_service: UserService
    token_service: TokenService
    hash_handler: HashHandler
    format_handler: FormatHandler

    def __init__(self) -> None:       
        self.user_service = UserService()
        self.token_service = TokenService()
        
        self.hash_handler = HashHandler()
        self.format_handler = FormatHandler()

    def _create_response(self, message: str, success: bool, data: dict = None) -> JSONResponse:
        response = dto.ResponseMessage(message=message, success=success, data=data)
        return JSONResponse(asdict(response))