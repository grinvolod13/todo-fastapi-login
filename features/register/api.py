from fastapi import APIRouter
from core.domain.model import User
from .domain.usecases import RegisterUserUseCase


from core.data.repository import UserRepositoryTest


router = APIRouter()

repo = UserRepositoryTest([])

@router.post("/register")
def register(user: User):
    return RegisterUserUseCase(repo).execute(user)

@router.get("/register")
def list_users():
    return repo.db