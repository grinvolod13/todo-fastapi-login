from core.domain import UseCase
from core.data.repository.user_repository import UserRepositoryAbstract
from core.domain.model import User
import bcrypt


class RegisterUserUseCase(UseCase):
    def __init__(self, repo: UserRepositoryAbstract, dependency: dict | None = None):
        self.repo = repo
        self.dependency = dependency
        
    def execute(self, user: User) -> bool:
        # TODO : set normal password checks and tests
        if (self.repo.get(user.username)!=None) or (self.repo.get_by_email(user.email)!=None):
            return False # if exists
        self.repo.add(user)
        return True
        
        
            
        
        