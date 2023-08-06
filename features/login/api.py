from fastapi import APIRouter, Depends, Response
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordRequestForm
from core.data.dependency import config, get_db
from features.login.domain.usecases import GetUserUseCase
from core.data.repository import UserRepositorySqlalchemy 
from bcrypt import checkpw
from sqlalchemy.orm.session import Session

login_manager = LoginManager(config['SECRET'], token_url="/login")

router = APIRouter()

@login_manager.user_loader()
def get_user(username: str, db:Session):
    repo = UserRepositorySqlalchemy(db)
    return GetUserUseCase(repo).execute(username)

@router.post("/login")
def login(data: OAuth2PasswordRequestForm=Depends(), db=Depends(get_db)):
    user = get_user(data.username, db=db)
    if not user:
        raise InvalidCredentialsException
    if checkpw(data.password.encode("utf-8"), user.password):
        token = login_manager.create_access_token(data=dict(sub=user.username))
        return {'access_token': token}
    
    
    raise InvalidCredentialsException

@router.get("/", dependencies=[Depends(login_manager)])
def main():
    return {"message": "success"}


    