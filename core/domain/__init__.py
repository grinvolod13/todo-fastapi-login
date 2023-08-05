from abc import ABC
from core.data import Repository

class UseCase(ABC):
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self):
        raise NotImplementedError()