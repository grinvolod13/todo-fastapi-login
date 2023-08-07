from core.data.repository.user_repository import UserRepositorySqlalchemy
from core.data.repository.todo_repository import TodoRepositorySqlalchemy
from features.todo.domain.model import Todo, Base
from core.domain.model import User
import pytest
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from core.data.orm import start_mappers
connection_string = "sqlite:///test.db"
test_engine = create_engine(connection_string)


start_mappers()

Base.metadata.create_all(test_engine)

users = [User(
    username="user {i}",
    email=f"email {i}",
    password=f"password {i}") for i in range(1, 11)]

todos = [Todo(
    username="todo {i}",
    description=f"todo {i} description",
    is_done=False,
    user=users[i-1]
    ) for i in range(1, 11)]




@pytest.fixture
def repo() -> TodoRepositorySqlalchemy:
     with Session(test_engine) as db:
        db.add_all(users)
        db.add_all(todos)
        db.flush()
        repo = TodoRepositorySqlalchemy(db)
        yield repo
        db.rollback()
        
        
def test_list_all(repo):
    result = repo.get_all()
    assert len(result) == 10