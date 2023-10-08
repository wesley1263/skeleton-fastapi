from typing import TypeVar

from pydantic import BaseModel

from app.abstracts.base_usecase import BaseUseCase
from app.exceptions.usecase_exception import UseCaseException
from app.interfaces.repository_interface import RepositoryInterface
from app.modules.core.messages_enum import MessagesEnum
from app.modules.user import schema

T = TypeVar("T")
P = TypeVar("P")


class LoginUseCase(BaseUseCase):
    def __init__(
            self,
            payload: BaseModel,
            repository: RepositoryInterface,
            schema: BaseModel,
            authorize: T,
            hash_pass: P,
    ):
        super().__init__(payload, repository, schema)
        self._authorize = authorize
        self._hash_pass = hash_pass

    async def _validate(self):
        user = await self._repository.get_one_by(email=self._payload.email)
        if not user:
            raise UseCaseException(MessagesEnum.USER_NOT_FOUND.value, 404)
        return user

    async def _serializer(self, user):
        access_token = self._authorize.create_access_token(subject=user.email)
        return {
            "email": user.email,
            "access_token": access_token,
        }

    async def execute(self):
        user = await self._validate()
        if not self._hash_pass.verify(self._payload.password, user.password):
            raise UseCaseException(MessagesEnum.INVALID_PASSWORD.value, 400)
        user_serialized = await self._serializer(user)
        return self._schema(**user_serialized)
