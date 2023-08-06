from copy import copy, deepcopy

from sqlalchemy import and_, delete, exists, select, or_
from core.data import Repository
from core.domain.model import User
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class UserRepositoryAbstract(Repository, ABC): # pragma: no cover
    def __init__(self, db):
        self.db = db
        
    def get(self, username) -> User | None:
        raise NotImplementedError()
    
    def add(self, user: User) -> User | None:
        raise NotImplementedError()
    
    def remove(self, user: User):
        raise NotImplementedError()
    
    def get_by_email(self, email) -> User | None:
        raise NotImplementedError()
    
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
    
    
    
class UserRepositorySqlalchemy(UserRepositoryAbstract):
    def __init__(self, db: Session): # pragma: no cover
        self.db: Session = db
        
    def get(self, username) -> User | None:
        result = self.db.execute(select(User).
                                 where(User.username==username)
                                 ).scalar_one_or_none()
        return result
    
    def add(self, user: User) -> User | None:
        if user is None or self.db.query(exists().
                           where(or_(User.username == user.username,
                                     User.email == user.email))).scalar():
            return None
        self.db.add(user)
        return user
    
    def remove(self, user: User) -> User | None:
        if user is None or not self.db.query(exists().
                           where(or_(User.username == user.username,
                                     User.email == user.email))).scalar():
            return None
        
        
        self.db.execute(delete(User).where(and_(User.email==user.email,
                                            User.username==user.username)))
        return user
    
    def get_by_email(self, email) -> User | None:
        result = self.db.execute(select(User).
                                 where(User.email==email)
                                 ).first()
        if result:
            result = result[0]
        return result
            
            

    
        

    
    