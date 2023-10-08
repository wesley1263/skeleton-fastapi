from app.exceptions.usecase_exception import UseCaseException
from app.interfaces.repository_interface import RepositoryInterface
from app.modules.core.messages_enum import MessagesEnum

from .. import schema


class GetUserUseCase:
    def __init__(self, id: int, repository: RepositoryInterface):
        self._id = id
        self._repository = repository

    async def _validate(self):
        user = await self._repository.get_by_id(self._id)
        if not user:
            raise UseCaseException(MessagesEnum.USER_NOT_FOUND.value, 404)
        return user

    async def execute(self):
        user = await self._validate()
        return schema.GetUserSchema.from_orm(user)
