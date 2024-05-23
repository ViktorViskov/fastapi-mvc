from datetime import datetime

from pydantic import BaseModel

# USER
class CreateUser(BaseModel):
    name: str
    surname: str
    email: str
    password: str

class GetUser(BaseModel):
    id: int
    name: str
    surname: str
    role: str
    email: str
    updated_at: datetime
    created_at: datetime        
    
class UpdateUser(BaseModel):
    name: str
    surname: str
    
class LoginUser(BaseModel):
    email: str
    password: str
    
class UpdateUserPass(BaseModel):
    old_password: str
    new_password: str

class ResetUserPass(BaseModel):
    email: str
    
# Token
class Token(BaseModel):
    id: int
    user_id: int
    hash: str
    created_at: datetime
    expired_at: datetime
