from app.abstracts.base_repository import AbstractTortoiseRepository
from app.modules.user.model import User


class UserRepository(AbstractTortoiseRepository):
    def __init__(self):
        super().__init__(User)
