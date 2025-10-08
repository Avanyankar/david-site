from sqlalchemy import Column, Integer, String
from db.database import Base

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
