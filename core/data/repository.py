from copy import copy, deepcopy
from core.data import Repository
from core.domain.model import User
from abc import ABC, abstractmethod



class UserRepositoryAbstract(Repository, ABC): # pragma: no cover
    def __init__(self, db):
        self.db = db
        
    @abstractmethod
    def get(self, username) -> User | None:
        raise NotImplementedError()
    
    @abstractmethod
    def add(self, user: User) -> User | None:
        raise NotImplementedError()
    
    @abstractmethod
    def remove(self, user: User):
        raise NotImplementedError()
    
    @abstractmethod
    def get_by_email(self, email) -> User | None:
        raise NotImplementedError()
    
    @abstractmethod
    def exists(self, user: User) -> bool:
        raise NotImplementedError()
    
    
    
class UserRepositoryTest(UserRepositoryAbstract):
    def __init__(self, db: list[User]):
        self.db = db
        
    def get(self, username) -> User | None:
        search = [user for user in self.db if user.username == username]
        if search:
            return copy(search[0])
        return None
        
    def add(self, user: User) -> User | None:
        checks = [_user for _user in self.db if (_user.username == user.username or _user.email == user.email)]
        if checks:
            return None
        self.db.append(copy(user))
        return user
    
    def remove(self, user: User) -> User | None:
        try:
            self.db.remove(user)
            return user
        except ValueError:
            return None
        
    def get_by_email(self, email) -> User | None:
        search = [user for user in self.db if user.email == email]
        if search:
            return copy(search[0])
        return None

    
    