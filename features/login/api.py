from fastapi import APIRouter, Depends
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.security import OAuth2PasswordRequestForm
from core.data.dependency import get_db
from features.login.domain.usecases import GetUserUseCase
from core.data.repository import UserRepositorySqlalchemy 
from sqlalchemy.orm.session import Session

from core.application.security import login_manager, check_password_hash


router = APIRouter()

@login_manager.user_loader(db=next(get_db()))
def get_user(username: str, db: Session):
        repo = UserRepositorySqlalchemy(db)
        return GetUserUseCase(repo).execute(username)

@router.post("/login")
def login(data: OAuth2PasswordRequestForm=Depends(), db=Depends(get_db)):
    
    user = get_user(data.username, db)
    if not user:
        raise InvalidCredentialsException
    if check_password_hash(data.password, user.password):
        token = login_manager.create_access_token(data=dict(sub=user.username))
        return {'access_token': token}
    
    raise InvalidCredentialsException



    