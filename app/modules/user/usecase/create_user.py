from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel

from app.abstracts.base_usecase import BaseUseCase
from app.exceptions.usecase_exception import UseCaseException
from app.interfaces.repository_interface import RepositoryInterface
from app.modules.core.messages_enum import MessagesEnum


class CreateUserUseCase(BaseUseCase):
    def __init__(
        self, payload: BaseModel, repository: RepositoryInterface, schema: BaseModel
    ):
        super().__init__(payload, repository)
        self._schema = schema

    async def _validate_email(self):
        user = await self._repository.get_one_by(email=self._payload.email)
        if user:
            raise UseCaseException(MessagesEnum.EMAIL_ALREADY_EXIST.value, 400)

    async def execute(self):
        await self._validate_email()

        self._payload.password = pbkdf2_sha256.hash(self._payload.password)
        user = await self._repository.create(self._payload.dict())
        return self._schema.from_orm(user)
