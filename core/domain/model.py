from dataclasses import dataclass

from sqlalchemy import Column, String
from core.application import security
from core.data.orm import Base
@dataclass
class User(Base):
    __tablename__ = 'user'
    
    username: str = Column(String(20), primary_key=True)
    email: str = Column(String(50), unique=True)
    password: bytes = Column(String(60), nullable=False)
    
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = security.generate_password_hash(password)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, User):
            return False
        return self.username == __value.username and self.email == __value.email
    