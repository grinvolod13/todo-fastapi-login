from fastapi import APIRouter
from fastapi_login import LoginManager


login_manager = LoginManager("secret", token_url="/login")

router = APIRouter()

@router.post("/login")
def login():
    ...