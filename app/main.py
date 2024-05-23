from fastapi import FastAPI

from controllers import auth_controller
from controllers import page_controller
from controllers import user_controller
from controllers import private_controller

from middlewares import cors_middleware
from middlewares import static_middleware


app = FastAPI()

cors_middleware.add(app)
static_middleware.add(app)

app.include_router(auth_controller.router)
app.include_router(page_controller.router)
app.include_router(user_controller.router)
app.include_router(private_controller.router)

