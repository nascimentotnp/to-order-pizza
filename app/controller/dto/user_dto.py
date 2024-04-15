from pydantic import BaseModel
from typing import Optional


class CreateUserDto(BaseModel):
    name: str
    email: str
    password: str


class UpdateUserDto(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
