from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_active: bool = True

    class Config:
        orm_mode = True
