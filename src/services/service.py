from sqlalchemy.orm import Session
from ..schemas import dimburo_service
from ..main import models
from ..main.utils import hash_password

class UserService:
    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()
    
    @staticmethod
    def create_user(db: Session, user: dimburo_service.UserCreate):
        hashed_password = hash_password(user.password)
        db_user = models.User(
            email=user.email, 
            name=user.name,
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user