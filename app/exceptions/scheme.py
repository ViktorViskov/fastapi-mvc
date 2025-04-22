class AppException(Exception):
    """Base class for all exceptions in the app."""

    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code