from fastapi import FastAPI

from middlewares import AuthMiddleware
from middlewares import static_middleware
from middlewares import cors_middleware

from routers import AuthRouter
from routers import ApiRouter
from routers import PublicPagesRouter
from routers import PrivatePagesRouter
from routers import ErrorPageRouter


# Apps
app = FastAPI()
private = FastAPI(docs_url=None, redoc_url=None)
api = FastAPI()

# middleware
cors_middleware(app)
AuthMiddleware(api)
AuthMiddleware(private)

# routes
AuthRouter(app)
PublicPagesRouter(app)
ErrorPageRouter(app)

PrivatePagesRouter(private)
ErrorPageRouter(private)

ApiRouter(api)
ErrorPageRouter(api)

# mounting
app.mount("/api", api)
app.mount("/private", private)
static_middleware(app)