from fastapi import FastAPI
from features.login.api import router as login_router
from core.data.orm import start_mappers

def create_app():
    app = FastAPI()
    start_mappers()
    
    app.include_router(login_router)
    return app    
    
