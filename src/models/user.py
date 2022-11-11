from .common import *


class UserBasic(BasicModel):
    name: str
    email: str

class UserRegistrationInput(UserBasic):
    password: str

class User(UserRegistrationInput):
    user_id: str = ""
    registration_date: str = ""
    role_type: str = ""
    
class UserLoginInput(BasicModel):
    email: str
    password: str
    
class UserResponse(UserBasic):
    user_id: str = ""
    registration_date: str = ""
    role_type: str = ""
    