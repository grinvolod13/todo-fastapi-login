from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from core.data.repository.user_repository import UserRepositorySqlalchemy
from core.domain.model import User
import core.data.dependency as dependency
from core.application.security import login_manager

router = APIRouter()


@router.get("/todo")
def list_tasks(db = Depends(dependency.get_db), user = Depends(login_manager)):
    return {"lol kek yes": "yes"}
    # return HTTPException(status_code=403, detail="Forbidden"


