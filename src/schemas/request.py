from pydantic import BaseModel

class RequestCreate(BaseModel):
    fullname: str
    phonenumber: int