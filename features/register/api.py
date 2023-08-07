from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from core.domain.model import User
from .domain.usecases import RegisterUserUseCase
import core.data.dependency as dependency
from core.application.security import login_manager

from core.data.repository.user_repository import UserRepositorySqlalchemy


router = APIRouter()


@router.post("/register")
def register(user: [str, str, str], db = Depends(dependency.get_db)):
    repo = UserRepositorySqlalchemy(db)
    return RegisterUserUseCase(repo).execute(User(user['username'], user['email'], user['password']))

@router.get("/register")
def list_users(db = Depends(dependency.get_db), user = Depends(login_manager)):
    if user.username == 'admin':
        repo = UserRepositorySqlalchemy(db)
        return repo.db.execute(select(User)).scalars().fetchall()
    return HTTPException(status_code=403, detail="Forbidden")