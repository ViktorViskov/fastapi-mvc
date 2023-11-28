from datetime import datetime

from fastapi.responses import JSONResponse
from fastapi.requests import Request

from models import dto
from models import other
from .base_controller import BaseController



class AuthController(BaseController):
    cookies_name = "session_token"
    session_ttl = 3600 * 24 * 7
    
    def validate_token(self, token_hash: str) -> bool:      
        is_valid = True
        
        now =  datetime.utcnow()
        token = self.token_service.get_by_hash(token_hash)
        
        if not token:
            is_valid = False
            
        # delete expired token
        if token and token.expired_at < now:
            self.token_service.delete(token.id)
            is_valid = False

        return is_valid
    
    def register(self, dto: dto.CreateUser) -> JSONResponse:
        response_message = ""
        response_success = False
        response_data = {}
        
        email = self.format_handler.format_email(dto.email)
        password = self.hash_handler.hash_password(dto.password)
        
        if not email:
            response_message = "Email can not be empty"
            return self._create_response(response_message, response_success, response_data)
        
        if not dto.password:
            response_message = "Password can not be empty"
            return self._create_response(response_message, response_success, response_data)
        
        exist_user = self.user_service.get_by_email(email)
        if exist_user:
            response_message = f"User {email} exist"
            return self._create_response(response_message, response_success, response_data)
        
        self.user_service.create(
            dto.name,
            dto.surname,
            other.Role.USER,
            email,
            password
        )
        response_success = True

        return self._create_response(response_message, response_success, response_data)

    def login(self, dto: dto.LoginUser) -> JSONResponse:
        response_message = ""
        response_success = True
        response_data = {}
        
        email = self.format_handler.format_email(dto.email)
        password = self.hash_handler.hash_password(dto.password)
        now =  datetime.utcnow()
        
        user = self.user_service.get_by_email_and_pass(email, password)
        if not user:
            response_message = "Login or password wrong"
            response_success = False
            return self._create_response(response_message, response_success, response_data)
        
        # get and delete all expired users tokens
        user_tokens = self.token_service.get_by_user_id(user.id)
        self.token_service.delete_expired(user_tokens)
        
        # create new token
        token_hash = self.hash_handler.generate_hash()
        valid_to = datetime.utcfromtimestamp(now.timestamp() + self.session_ttl)
        new_token = self.token_service.create(user, token_hash, valid_to)
        
        token_expired_at: datetime = new_token.expired_at
        token_ttl = int(token_expired_at.timestamp() - now.timestamp())
            
        response = self._create_response(response_message, response_success, response_data)
        response.set_cookie(self.cookies_name, new_token.hash, token_ttl)
            
        return response

    def logout(self, req: Request) -> JSONResponse:
        token_hash = req.cookies.get(self.cookies_name, "")
        
        response_message = "Session not found"
        response_success = False
        response_data = {}
        
        token = self.token_service.get_by_hash(token_hash)
        if token:
            response_message = ""
            response_success = True
            self.token_service.delete(token)
        
        return self._create_response(response_message, response_success, response_data)

    def check_session(self, req: Request) -> JSONResponse:
        token_hash = req.cookies.get(self.cookies_name, "")
        
        is_valid = self.validate_token(token_hash)
        response = JSONResponse(is_valid)
        
        if not is_valid:
            response.delete_cookie(self.cookies_name)

        return response