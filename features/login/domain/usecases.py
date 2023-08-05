from core.domain import UseCase
from core.data.repository import UserRepositoryAbstract
from core.domain.model import User
import bcrypt

class VerifyUserUseCase(UseCase):
    def __init__(self, repo: UserRepositoryAbstract, dependency: dict):
        self.repo = repo
        self.dependency = dependency
        
    def execute(self, user: User) -> bool:
        user_from_repo : User = self.repo.get_user(user.username)
        if user_from_repo and bcrypt.checkpw(user.password, user_from_repo.password):
            return True
        return False

        
        
        