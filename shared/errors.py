### shared/errors.py

class BaseCanvasError(Exception):
    def __init__(self, message="An unknown error occurred."):
        super().__init__(message)
        self.message = message

class ValidationError(BaseCanvasError):
    pass

class AuthorizationError(BaseCanvasError):
    pass

class ResourceNotFoundError(BaseCanvasError):
    pass