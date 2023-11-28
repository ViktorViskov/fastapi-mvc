from controllers import AuthController
from controllers import UserController
from controllers import PageController


class BaseRouter:
    auth_controller: AuthController
    user_controller: UserController
    page_controller: PageController
    
    def __init__(self) -> None:
        self.auth_controller = AuthController()
        self.user_controller = UserController()
        self.page_controller = PageController()