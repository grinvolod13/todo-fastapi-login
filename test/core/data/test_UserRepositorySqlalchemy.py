from core.data.repository import UserRepositorySqlalchemy
from core.domain.model import User
import pytest
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from core.data.orm import start_mappers, metadata


connection_string = "sqlite:///test.db"
start_mappers()
test_engine = create_engine(connection_string)
metadata.create_all(test_engine)

users = [User(f"User_{i}", f"user_{i}@mail.com", f"password_{i}") for i in range(10)]

@pytest.fixture
def repo() -> UserRepositorySqlalchemy:
     with Session(test_engine) as db:
        db.add_all(users)
        db.flush()
        repo = UserRepositorySqlalchemy(db)
        yield repo
        db.rollback()
        
         
    



def test_get_success(repo: UserRepositorySqlalchemy):
    assert repo.get("User_0") == users[0]
        
def test_get_fail(repo: UserRepositorySqlalchemy):
    assert repo.get("Unknown user") == None
        
def test_get_by_email_success(repo: UserRepositorySqlalchemy):
    assert repo.get_by_email("user_0@mail.com") == users[0]

def test_get_by_email_fail(repo: UserRepositorySqlalchemy):
    assert repo.get_by_email("not email") == None
    
def test_add_success(repo):
    new = User("new", "new", "new")
    assert new == repo.add(new)
    assert new == repo.get("new")
    
def test_add_fail(repo):
    new = User("User_0", "new", "new")
    assert repo.add(new) == None
    assert repo.get("new") == None
    
def test_remove_success(repo):
    existing = repo.get(users[0].username)
    
    assert repo.remove(existing) == users[0]
    assert repo.get(users[0].username) == None
    
def test_remove_fail(repo):
    not_existing = User("not exist", "", "")
    assert repo.remove(not_existing) == None
    
def test_get_by_email_success(repo):
    user = repo.get_by_email(users[0].email)
    assert user == users[0]

def test_get_by_email_fail(repo):
    user = repo.get_by_email("not email")
    assert user == None
    
    
    
