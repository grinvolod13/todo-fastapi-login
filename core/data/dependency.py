from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = dotenv_values(".env")

engine = create_engine(config['CONNECTION_STRING'])

def get_db():
    with sessionmaker(engine)() as db:
        yield db
        db.commit()
    

