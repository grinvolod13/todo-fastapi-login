from sqlalchemy import Column, MetaData, String, Table
from sqlalchemy.orm import mapper, registry, relationship, DeclarativeBase 
from ..domain import model


class Base(DeclarativeBase):
    ...


mapper_registry = registry(metadata=Base.metadata)



user = Table(
    'user',
    mapper_registry.metadata,
    Column('username', String(20), primary_key=True),
    Column('email', String(50), unique=True),
    Column('password', String(60), nullable=False),
)

def start_mappers(): # TODO: add tests
    user_mapper = mapper_registry.map_imperatively(
        model.User,
        user,
        properties={
            "todos": relationship("todo", back_populates="user")
            },
        
)