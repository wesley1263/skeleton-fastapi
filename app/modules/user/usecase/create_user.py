from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel

from app.abstracts.base_repository import BaseRepository
from app.abstracts.base_usecase import BaseUseCase
from app.abstracts.usecase_exception import UseCaseException
from app.modules.core.messages_enum import MessagesEnum


class CreateUserUseCase(BaseUseCase):
    def __init__(self, payload: BaseModel, repository: BaseRepository, schema: BaseModel):
        super().__init__(payload, repository)
        self._schema = schema

    async def _validate_email(self):
        user = await self._repository.get_by_email(self._payload.email)
        if user:
            raise UseCaseException(
                MessagesEnum.EMAIL_ALREADY_EXIST, 400
            )

    async def execute(self):
        await self._validate_email()

        self._payload.password = pbkdf2_sha256.hash(self._payload.password)
        user = await self._repository.create(self._payload.dict())
        return self._schema.from_orm(user)
