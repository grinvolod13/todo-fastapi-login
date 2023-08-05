import pytest
from core.application import security
import bcrypt

def test_generate_password_hash():
    password: str = 'password'
    hashed_test = security.generate_password_hash(password)
    salt = hashed_test[:29]
    assert hashed_test == bcrypt.hashpw(password.encode('utf-8'), salt)
    
    
def test_check_password_hash_success():
    password_bytes: bytes = ('password').encode('utf-8')
    password_hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    assert security.check_password_hash('password', password_hashed)
    
    
def test_check_password_hash_fail():
    password_hashed = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
    assert False == security.check_password_hash("wrong_password", password_hashed)
