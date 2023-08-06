from core.data.repository.user_repository import UserRepositoryTest
from core.domain.model import User
import pytest
from copy import deepcopy



start_db = [User(f"User_{i}", f"user_{i}@mail.com", f"password_{i}") for i in range(10)]
    
    



def test_init():
    repo = UserRepositoryTest(deepcopy(start_db))
    assert repo.db == start_db
    
def test_add_success():
    repo = UserRepositoryTest(deepcopy(start_db))
    user = User("User_10", "user_10@mail.com", "password_10")
    out = repo.add(deepcopy(user))
    assert len(repo.db) == len(start_db) + 1
    assert repo.db[-1] == user
    assert out == user
    

def test_add_fail():
    repo = UserRepositoryTest(deepcopy(start_db))
    user = User("User_9", "user_9@mail.com", "password_9")
    out = repo.add(deepcopy(user))
    assert len(repo.db) == len(start_db)
    assert out == None

def test_get_success():
    repo = UserRepositoryTest(deepcopy(start_db))
    user = repo.get("User_0")
    assert user == start_db[0]
    
def test_get_fail():
    repo = UserRepositoryTest(deepcopy(start_db))
    user = repo.get("not_a_user")
    assert user == None

def test_get_by_email_success():
    repo = UserRepositoryTest(deepcopy(start_db))
    user = repo.get_by_email("user_0@mail.com")
    assert user == start_db[0]
    
def test_get_by_email_fail():
    repo = UserRepositoryTest(deepcopy(start_db))
    user = repo.get_by_email("not_a_user@mail.com")
    assert user == None
    
def test_remove_success():
    repo = UserRepositoryTest(deepcopy(start_db))
    user = repo.get("User_0")
    out = repo.remove(user)
    assert len(repo.db) == len(start_db) - 1
    assert user == out
    user_rm = repo.get("User_0")
    assert user_rm == None
    
def test_remove_fail():
    repo = UserRepositoryTest(deepcopy(start_db))
    user = User("User_10", "", "")
    out = repo.remove(user)
    assert len(repo.db) == len(start_db)
    assert out == None
    
# def test_exists_success():
#     repo = UserRepositoryTest(deepcopy(start_db))
#     user_1 = User("User_0", "OTHER MAIL", "password_0")
#     user_2 = User("OTHER NAME", "user_0@mail.com", "password_0")
#     assert repo.exists(user_1) == True
#     assert repo.exists(user_2) == True
#     assert len([u for u in start_db if (user.email == u.email) or (user.username == u.username)]) != 0
    
# def test_exists_fail():
#     repo = UserRepositoryTest(deepcopy(start_db))
#     user = User("User_10", "user_10@mail.com", "password_0")
#     out = repo.exists(user)
#     assert out == False
#     assert len([ u for u in start_db if (user.email == u.email) or (user.username == u.username)]) > 0
    
    
    