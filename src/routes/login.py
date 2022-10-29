import os

import jwt
from db.user import find_user_with_email
from fastapi import APIRouter, HTTPException
from models import UserLoginInput
from passlib.hash import argon2
from starlette.responses import JSONResponse

router = APIRouter(tags=["Login"])

@router.post("/")
def login_with_email(input: UserLoginInput):
    user = find_user_with_email(input.email)
    if user==None:
        raise HTTPException(401,"Unauthorized")
    if not argon2.verify(input.password,user.password):
        raise HTTPException(401,"Unauthorized")
    encoded_jwt = jwt.encode({"user_id": user.user_id, "role": user.role_type}, os.environ.get("JWT_SECRET"), algorithm="HS256")
    return JSONResponse("Success", headers={
        "token": encoded_jwt
    })
