from fastapi import FastAPI
from fastapi.requests import Request

from .base_router import BaseRouter


class PublicPagesRouter(BaseRouter):
    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self._init_routes(app)
        
    def _init_routes(self, app: FastAPI) -> None:
        @app.get("/")
        def main_page(req: Request):
            return self.page_controller.main()
        
        @app.get("/login")
        def main_page(req: Request):
            return self.page_controller.login()
        
        @app.get("/register")
        def main_page(req: Request):
            return self.page_controller.register()
        
        @app.get("/forgot")
        def main_page(req: Request):
            return self.page_controller.forgot_password()


