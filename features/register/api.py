from fastapi import APIRouter, Depends
from sqlalchemy import select
from core.domain.model import User
from .domain.usecases import RegisterUserUseCase
import core.data.dependency as dependency

from core.data.repository import UserRepositorySqlalchemy


router = APIRouter()


@router.post("/register")
def register(user: User, db = Depends(dependency.get_db)):
    repo = UserRepositorySqlalchemy(db)
    return RegisterUserUseCase(repo).execute(user)

@router.get("/register")
def list_users(db = Depends(dependency.get_db)):
    repo = UserRepositorySqlalchemy(db)
    return repo.db.execute(select(User)).scalars().fetchall()