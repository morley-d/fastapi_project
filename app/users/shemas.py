from datetime import date
from pydantic import BaseModel, EmailStr


class ShemaUserRegister(BaseModel):
    email: EmailStr
    password: str
