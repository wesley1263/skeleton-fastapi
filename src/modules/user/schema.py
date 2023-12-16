from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel


class GetUserSchema(CamelModel):
    id: int
    email: str
    name: str
    is_active: bool = True
    crate_at: Optional[datetime] = None
    update_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class PostUserSchema(CamelModel):
    name: str
    email: str
    password: str
    is_active: bool = True


class UpdateUserSchema(CamelModel):
    name: str
    email: str
    password: str
    is_active: bool = True


class LoginUserSchema(CamelModel):
    email: str
    password: str


class JWTUserSchema(CamelModel):
    email: str
    access_token: str


class SimpleMessageSchema(CamelModel):
    message: str
