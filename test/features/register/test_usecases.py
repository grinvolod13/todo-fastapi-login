import pytest
from core.data.repository.user_repository import UserRepositoryTest
from core.application import security
from core.domain.model import User
from features.register.domain.usecases import (RegisterUserUseCase)






@pytest.fixture
def repo():
    start_db = [User(f"User_{i}",
                 f"user_{i}@mail.com",
                 f"password_{i}",
                 ) for i in range(10)]
    yield UserRepositoryTest(start_db)




def test_register_success(repo):
    user = User("User_New","new@mail.com","password_new")
    result = RegisterUserUseCase(repo).execute(user)
    assert result == True
    assert repo.get("User_New") == user
    
def test_register_not_unique_username_fail(repo):
    user = User("User_0","new@mail.com","password_0")
    result = RegisterUserUseCase(repo).execute(user)
    assert result == False
    assert repo.get("User_0") != user

def test_register_not_unique_email_fail(repo):
    user = User("User_New","user_0@mail.com","password_0")
    result = RegisterUserUseCase(repo).execute(user)
    # print(user)
    # print(repo.get_by_email("User_0@mail.com"))
    assert result == False
    assert repo.get_by_email("user_0@mail.com") != user
    
    
    