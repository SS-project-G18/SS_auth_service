from datetime import datetime
from uuid import uuid4

from db.user import add_user, find_user_with_email
from fastapi import APIRouter, HTTPException
from models import User, UserRegistrationInput
from passlib.hash import argon2
from starlette.responses import JSONResponse

router = APIRouter(tags=["Registration"])


@router.post("/")
def register_user(input: UserRegistrationInput):
    if find_user_with_email(input.email)!=None:
        raise HTTPException(400, "User with given credentials exists")
    model = User(**input.__dict__)
    model.password = argon2.using(rounds=4).hash(model.password)
    model.user_id==uuid4()
    model.role_type=="User"
    model.registration_date=datetime.utcnow()
    add_user(model)
    return JSONResponse("Success")
