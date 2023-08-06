from fastapi import FastAPI
from features.login.api import router as login_router
from features.register.api import router as register_router

def create_app():
    app = FastAPI()
    
    app.include_router(login_router)
    app.include_router(register_router)
    return app    
    
