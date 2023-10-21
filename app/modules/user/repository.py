from pydantic import BaseModel
from tortoise.exceptions import BaseORMException

from app.abstracts.create_repository import CreateRepository
from app.abstracts.retrieve_all_repository import RetrieveAllRepository
from app.abstracts.retrieve_one_by_repository import RetrieveOneByRepository
from app.abstracts.update_repository import UpdateRepository
from app.modules.user.entity import UserEntity
from app.modules.user.model import User


class UserRepository(
    CreateRepository, RetrieveAllRepository, RetrieveOneByRepository, UpdateRepository
):
    def __init__(self):
        super().__init__(User, UserEntity)

    async def get_by_id(self, id: int) -> [BaseModel, None]:
        try:
            _result = await self.get_one_by(id=id)
            if not _result:
                return None
            return self._model.from_orm(_result)
        except BaseORMException:
            return None
