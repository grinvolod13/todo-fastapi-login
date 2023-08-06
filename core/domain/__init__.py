from abc import ABC
from core.data import Repository

class UseCase(ABC): # pragma: no cover
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self):
        raise NotImplementedError()