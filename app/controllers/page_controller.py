from fastapi.responses import FileResponse


class PageController:
    templates_path: str
    
    def __init__(self) -> None:
        self.templates_path = "templates"
        
    def _read_page(self, name: str) -> FileResponse:
        return FileResponse(f"{self.templates_path}/{name}")
    
    def not_found(self) -> FileResponse:
        return self._read_page("404.html")
    
    def not_authorized(self) -> FileResponse:
        return self._read_page("403.html")

    def forgot_password(self) -> FileResponse:
        return self._read_page("forgot.html")
    
    def login(self) -> FileResponse:
        return self._read_page("login.html")
    
    def register(self) -> FileResponse:
        return self._read_page("register.html")
    
    def private(self) -> FileResponse:
        return self._read_page("private.html")
    
    def main(self) -> FileResponse:
        return self._read_page("main.html")