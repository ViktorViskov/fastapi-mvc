from fastapi import FastAPI
from fastapi import Request
from fastapi import Response

from controllers import AuthController
from controllers import PageController


class AuthMiddleware:
    app: FastAPI
    auth_controller: AuthController
    page_controller: PageController

    def __init__(self, server: FastAPI) -> None:
        self.auth_controller = AuthController()
        self.page_controller = PageController()

        self._add_auth_middleware(server)

    def _add_auth_middleware(self, app: FastAPI):
        @app.middleware("http")
        async def middleware(req: Request, call_back):
            token = req.cookies.get(self.auth_controller.cookies_name)
            response: Response

            if token and self.auth_controller.validate_token(token):
                response = await call_back(req)
            else:
                # response = Response(status_code=401)
                response = self.page_controller.not_authorized()
                response.delete_cookie(self.auth_controller.cookies_name)

            return response
