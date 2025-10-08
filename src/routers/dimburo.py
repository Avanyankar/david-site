from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.request import RequestCreate
from services.request_service import create_request
from dependencies import get_db

router = APIRouter(prefix="/dimburo", tags=["dimburo"])

@router.post("/", response_model=RequestCreate)
def create_new_request(request: RequestCreate, db: Session = Depends(get_db)):
    return create_request(db, request)
