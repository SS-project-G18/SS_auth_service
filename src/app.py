from db.user import find_user_with_email
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import argon2
from routes import login, registration, user
from routes.utils import create_access_token

app = FastAPI()

app.include_router(login.router, prefix="/login")
app.include_router(registration.router, prefix="/registration")
app.include_router(user.router, prefix="/user")


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = find_user_with_email(form_data.username)
    if user==None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not argon2.verify(form_data.password,user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    data = {"user_id": user.user_id}
    encoded_jwt = create_access_token(data)
    return {"access_token": encoded_jwt, "token_type": "bearer"}