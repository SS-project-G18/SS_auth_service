from fastapi import FastAPI

from routes import login, registration

app = FastAPI()

app.include_router(login.router, prefix="/login")
app.include_router(registration.router, prefix="/registration")
