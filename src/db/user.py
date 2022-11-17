from models import User, UserResponse

from . import users_db


def find_user_with_email(email):
    user = users_db.find_one({"email": email})
    if user!=None:
        return User.parse_obj(user)
    
def add_user(input: User):
    users_db.insert_one(input.to_json())

def get_user_with_id(user_id):
    user = users_db.find_one({"user_id": user_id})
    if user!=None:
        return User.parse_obj(user)
    
def db_get_all_users():
    res = users_db.find({})
    return [UserResponse.parse_obj(x) for x in res]

def db_update_user_password(user_id, new_pass):
    users_db.update_one({"user_id": user_id}, {
        "$set": {
            "password": new_pass
        }
    })
    