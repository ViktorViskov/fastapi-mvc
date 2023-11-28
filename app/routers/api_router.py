from fastapi import FastAPI
from fastapi.requests import Request

from .base_router import BaseRouter


class ApiRouter(BaseRouter):
    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self._init_routes(app)
        
    def _init_routes(self, app: FastAPI) -> None:
        @app.get("/users")
        def products(req: Request):
            return self.user_controller.get_all(1000, 0)

