from fastapi import FastAPI

from .base_router import BaseRouter


class ErrorPageRouter(BaseRouter):
    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self._init_routes(app)
        
    def _init_routes(self, app: FastAPI) -> None:
        # return on all not existing pages index.html file
        @app.exception_handler(404)
        async def not_found_page(request, exc):
            return self.page_controller.not_found()