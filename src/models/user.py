from sqlalchemy import Column, Integer, String, Boolean
from example_database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    is_admin = Column(Boolean)
