from fastapi import FastAPI
from features.login.api import router as login_router
from features.register.api import router as register_router
from features.todo.api import router as todo_router

def create_app():
    app = FastAPI()
    
    app.include_router(login_router)
    app.include_router(register_router)
    app.include_router(todo_router)
    return app    
    
