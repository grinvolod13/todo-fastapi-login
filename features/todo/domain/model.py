from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from core.data.orm import Base

class Todo(Base):
    __tablename__  = "todo"
    
    id: int = Column(Integer, autoincrement=True, primary_key=True)
    name: str = Column(String(100), nullable=False)
    description: str = Column(String(500), nullable=False, default="")
    is_done: bool = Column(bool, nullable=False, default=False)
    user: Mapped["User"] = relationship("user", back_populates="todo")

    
    
    


