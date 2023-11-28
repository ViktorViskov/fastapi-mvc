from fastapi import FastAPI
from fastapi.requests import Request

from models import dto
from .base_router import BaseRouter


class AuthRouter(BaseRouter):
    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self._init_routes(app)
        
    def _init_routes(self, app: FastAPI) -> None:
        @app.post("/login", response_model=dto.ResponseMessage)
        def login(req: Request, dto: dto.LoginUser):
            return self.auth_controller.login(dto)
        
        @app.post("/register", response_model=dto.ResponseMessage)
        def registration(req: Request, dto: dto.CreateUser):
            return self.auth_controller.register(dto)
        
        @app.get("/logout", response_model=dto.ResponseMessage)
        def logout(req: Request):
            return self.auth_controller.logout(req)
        
        @app.get("/validate", response_model=bool)
        def validate(req: Request):
            return self.auth_controller.check_session(req)
        
        @app.post("/reset_password", response_model=bool)
        def validate(req: Request, dto: dto.ResetUserPass):
            return self.user_controller.reset_password(dto.email)
        

   