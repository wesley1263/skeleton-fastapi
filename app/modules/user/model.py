from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
    is_active: bool = True

    class Config:
        orm_mode = True
