from sqlalchemy.orm import Session
from models.request import Request
from schemas.request import RequestCreate
from core.security import hash_password

def create_request(db: Session, request: RequestCreate):
    db_request = Request(requestname=request.requestname, password_hash=hash_password(request.password))
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request