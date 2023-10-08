from app.exceptions.usecase_exception import UseCaseException
from app.interfaces.repository_interface import RepositoryInterface
from app.modules.core.messages_enum import MessagesEnum
from app.modules.user import schema


class GetUserByEmailUseCase:
    def __init__(self, email: str, repository: RepositoryInterface):
        self._email = email
        self._repository = repository

    async def _validate(self):
        user = await self._repository.get_one_by(email=self._email)
        if not user:
            raise UseCaseException(MessagesEnum.USER_NOT_FOUND.value, 404)
        return user

    async def execute(self):
        user = await self._validate()
        return schema.GetUserSchema.from_orm(user)
