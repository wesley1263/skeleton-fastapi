from pydantic import BaseModel
from tortoise.exceptions import BaseORMException

from src.abstracts.create_repository import CreateRepository
from src.abstracts.retrieve_all_repository import RetrieveAllRepository
from src.abstracts.retrieve_one_by_repository import RetrieveOneByRepository
from src.abstracts.update_repository import UpdateRepository
from src.modules.user.entity import UserEntity
from src.modules.user.model import User


class UserRepository(
    CreateRepository, RetrieveAllRepository, RetrieveOneByRepository, UpdateRepository
):
    def __init__(self):
        super().__init__(User, UserEntity)

    async def get_by_id(self, id: int) -> [BaseModel, None]:
        try:
            _result, _ = await self.get_one_by(id=id)
            if not _result:
                return None
            return _result
        except BaseORMException:
            return None
