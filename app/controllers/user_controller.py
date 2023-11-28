from random import randint

from fastapi.responses import JSONResponse

from models import db
from models import dto
from .base_controller import BaseController


class UserController(BaseController):
    def get_all(self, limit: int, offset: int) -> list[db.User]:
        users = self.user_service.get(limit, offset)
        return [dto.GetUser(u.id, u.name, u.surname, u.role, u.email) for u in users]
        
            
    def get_by_id(self, id: int) -> db.User | None:
        return  self.user_service.get_by_id(id)
    
    def get_by_email(self, email: str) -> db.User | None:
        return  self.user_service.get_by_email(email)
    
    def get_by_token_hash(self, hash: str) -> db.User | None:
        user = None
        
        token = self.token_service.get_by_hash(hash)
        if token:
            user = self.user_service.get_by_id(token.user_id)
        
        return user
    
    def delete(self, user_id: int) -> JSONResponse:
        response_message = "User not found"
        response_success = False
        response_data = {}
        
        user = self.get_by_id(user_id)
        if user:
            response_message = f"User {user.email} deleted"
            response_success = True
            self.user_service.delete(user)
        
        return self._create_response(response_message, response_success, response_data)
    
    def update(self, dto: dto.UpdateUser) -> JSONResponse:
        response_message = "User not found"
        response_success = False
        response_data = {}
        
        user = self.user_service.get_by_id(dto.id)
        
        if user:
            user.name = dto.name
            user.surname = dto.surname
            
            user = self.user_service.update(user)
            
            response_message = "User updated"
            response_success = True
            
        return self._create_response(response_message, response_success, response_data)
    
    def update_password(self, dto: dto.UpdateUserPass) -> JSONResponse:
        response_message = "User not found"
        response_success = False
        response_data = {}
        
        old_password = self.hash_handler.hash_password(dto.old_password)
        new_password = self.hash_handler.hash_password(dto.new_password)
        
        user = self.user_service.get_by_id(dto.id)
        if not user:
            response_message = "User not found"
            return self._create_response(response_message, response_success, response_data)
        
        if not dto.old_password or not dto.new_password:
            response_message = "Password can not be empty"
            return self._create_response(response_message, response_success, response_data)
        
        if dto.old_password == dto.new_password:
            response_message = "Passwords can not be same"
            return self._create_response(response_message, response_success, response_data)
        
        if user.password != old_password:
            response_message = "Password is wrong"
            return self._create_response(response_message, response_success, response_data)
        
        user.password = new_password
        
        user = self.user_service.update(user)
        
        response_message = "Password updated"
        response_success = True
            
        return self._create_response(response_message, response_success, response_data)
    
    def reset_password(self, email: str) -> JSONResponse:
        response_message = "User not found"
        response_success = False
        response_data = {}
        
        new_password = ""
        user = self.user_service.get_by_email(email)
        if user:
            new_password = str(randint(100000, 999999))
            print(new_password)
            
            user.password = self.hash_handler.hash_password(new_password)
            self.user_service.update(user)
            
            response_message = "Password was reset"
            response_success = True
            
        return self._create_response(response_message, response_success, response_data)