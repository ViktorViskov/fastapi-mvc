from enum import IntEnum
from enum import StrEnum

   
class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"
