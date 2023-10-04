from app.abstracts.base_repository import BaseRepository
from app.modules.user.model import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = User

    async def get_by_email(self, email: str) -> [dict, None]:
        return await self.entity.get_or_none(email=email)
