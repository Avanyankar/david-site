from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..schemas import dimburo_service
from ..main import service
from ..dependencies import get_db, get_current_user

api_router = APIRouter()

@api_router.get("/users/{user_id}", response_model=dimburo_service.UserResponse)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: dimburo_service.UserResponse = Depends(get_current_user)
):
    user = service.UserService.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@api_router.post("/users/", response_model=dimburo_service.UserResponse)
async def create_user(
    user: dimburo_service.UserCreate,
    db: Session = Depends(get_db)
):
    return service.UserService.create_user(db, user)