from dataclasses import dataclass
from core.application import security

@dataclass
class User():
    username: str
    email: str
    password: bytes
    
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = security.generate_password_hash(password)

        
    