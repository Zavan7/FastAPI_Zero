from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str

class UserSchemas(BaseModel):
    user: str
    email: EmailStr
    password: str