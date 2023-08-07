from copy import copy

from sqlalchemy import and_, delete, exists, select, or_
from core.data import Repository
from features.todo.domain.model import Todo
from abc import ABC
from sqlalchemy.orm import Session

class TodoRepositoryAbstract(Repository, ABC): # pragma: no cover 
    def get_all(self):
        raise NotImplementedError()

    def get_by_name(self, name):
        raise NotImplementedError()

    def get(self, todo: Todo):
        raise NotImplementedError()

    def add(self, todo: Todo):
        raise NotImplementedError()

    def update(self, todo: Todo):
        raise NotImplementedError()

    def delete(self, todo: Todo):
        raise NotImplementedError()
    
class TodoRepositorySqlalchemy(TodoRepositoryAbstract):
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(Todo).all()