
from db.user import db_get_all_users
from fastapi import APIRouter, Depends, HTTPException
from models import User
from starlette.responses import JSONResponse

from .utils import get_current_user_admin

router = APIRouter(tags=["User"])

@router.get("/all")
def get_all_users(user: User = Depends(get_current_user_admin)):
    return db_get_all_users()
