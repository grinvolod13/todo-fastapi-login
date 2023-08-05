from dataclasses import dataclass
from core.application import security

@dataclass
class User():
    username: str
    email: str
    password: str | bytes
    
    def check_password(self, password: str | bytes) -> bool:
        return security.check_password(password, self.password)
    
    