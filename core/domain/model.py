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

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, User):
            return False
        return self.username == __value.username and self.email == __value.email
    