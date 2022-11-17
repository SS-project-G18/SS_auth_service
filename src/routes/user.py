
from db.user import db_get_all_users, db_update_user_password, get_user_with_id
from fastapi import APIRouter, Body, Depends, HTTPException
from models import User, UserInfo, UserPasswordUpdate
from passlib.hash import argon2
from starlette.responses import JSONResponse

from .utils import get_current_user, get_current_user_admin

router = APIRouter(tags=["User"])

@router.get("/all")
def get_all_users(user: User = Depends(get_current_user_admin)):
    return db_get_all_users()


@router.get("")
def get_current_user_info(user: User = Depends(get_current_user)):
    return UserInfo.parse_obj(user.dict())

@router.post("/reset/pass")
def update_password(user: User = Depends(get_current_user), input: UserPasswordUpdate = Body(description="New password to set ")):
    #Not taking the current pass as user is already authenticated
    if argon2.verify(input.password,user.password):
        raise HTTPException(302, "New Password cannot be same as the current one")
    db_update_user_password(user.user_id, argon2.using(rounds=4).hash(input.password))
    return "Success"