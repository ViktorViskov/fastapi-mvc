from fastapi import FastAPI
from fastapi.responses import FileResponse


TEMPLATE_PATH = 'templates'

def read_page(name: str) -> FileResponse:
    return FileResponse(f"{TEMPLATE_PATH}/{name}")

def set_not_found_page(app: FastAPI):
    @app.exception_handler(404)
    async def not_found_page(request, exc):
        return read_page("404.html")