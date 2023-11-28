from dataclasses import dataclass


@dataclass
class ResponseMessage:
    message: str
    success: bool
    data: dict

# USER
@dataclass
class CreateUser:
    name: str
    surname: str
    email: str
    password: str
    
@dataclass
class UpdateUser:
    id: int
    name: str
    surname: str
    
@dataclass
class LoginUser:
    email: str
    password: str
    
@dataclass
class UpdateUserPass:
    id: int
    old_password: str
    new_password: str

@dataclass
class ResetUserPass:
    email: str

@dataclass
class GetUser:
    id: int
    name: str
    surname: str
    role: str
    email: str
