from fastapi import FastAPI
from fastapi.requests import Request

from .base_router import BaseRouter


class PrivatePagesRouter(BaseRouter):
    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self._init_routes(app)
        
    def _init_routes(self, app: FastAPI) -> None:
        @app.get("/")
        def dashboard_page(req: Request):
            return self.page_controller.private()

