from app import create_app
from uvicorn import run
from core.data.orm import start_mappers

start_mappers()
app = create_app()