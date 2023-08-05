from core.domain import UseCase
from core.data.repository import UserRepositoryAbstract
from core.domain.model import User
import bcrypt


class RegisterUserUseCase(UseCase):
    def __init__(self, repo: UserRepositoryAbstract, dependency: dict | None = None):
        self.repo = repo
        self.dependency = dependency
        
    def execute(self, user: User) -> bool:
        ...
        