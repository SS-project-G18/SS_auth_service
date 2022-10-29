from models import User

from . import users_db


def find_user_with_email(email):
    user = users_db.find_one({"email": email})
    if user!=None:
        return User.parse_obj(user)
    
def add_user(input: User):
    users_db.insert_one(input.to_json())
