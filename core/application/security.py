import bcrypt
from fastapi_login import LoginManager
from core.data.dependency import config

def generate_password_hash(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password_hash(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


login_manager = LoginManager(config['SECRET'], token_url=config['TOKEN_URL'])




