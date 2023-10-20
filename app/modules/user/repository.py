from app.abstracts.base_repository import BaseTortoiseRepository
from app.modules.user.entity import UserEntity
from app.modules.user.model import User


class UserRepository(BaseTortoiseRepository):
    def __init__(self):
        super().__init__(User, UserEntity)
