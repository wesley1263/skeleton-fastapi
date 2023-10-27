from pydantic import BaseModel

from app.exceptions.usecase import UseCaseException
from app.interfaces.crud_repository import ICRUDRepository
from app.modules.core.messages_enum import MessagesEnum


class GetUserByEmailUseCase:
    def __init__(self, email: str, repository: ICRUDRepository, schema: BaseModel):
        self._email = email
        self._repository = repository
        self._schema = schema

    async def _validate(self):
        user, _ = await self._repository.get_one_by(email=self._email)
        if not user:
            raise UseCaseException(MessagesEnum.USER_NOT_FOUND.value, 404)
        return user

    async def execute(self):
        user = await self._validate()
        return self._schema(**user.dict())
