import os
from datetime import timedelta

import jwt
# from config import ACCESS_TOKEN_EXPIRE_MINUTES
from db.user import find_user_with_email
from fastapi import APIRouter, Depends, HTTPException
from models import UserLoginInput
from passlib.hash import argon2
from starlette.responses import JSONResponse

from .utils import create_access_token

router = APIRouter(tags=["Login"])

@router.post("/")
def login_with_email(input: UserLoginInput):
    user = find_user_with_email(input.email)
    if user==None:
        raise HTTPException(401,"Unauthorized")
    if not argon2.verify(input.password,user.password):
        raise HTTPException(401,"Unauthorized")
    data = {"user_id": user.user_id}
    encoded_jwt = create_access_token(data)
    return JSONResponse("Success", headers={
        "token": encoded_jwt
    })

