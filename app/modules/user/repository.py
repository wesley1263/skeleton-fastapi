from app.abstracts.base_repository import BaseRepository
from app.modules.user.model import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
