from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel

from app.abstracts.base_usecase import BaseUseCase
from app.exceptions.usecase import UseCaseException
from app.interfaces.crud_repository import ICRUDRepository
from app.modules.core.messages_enum import MessagesEnum


class UpdateUserUseCase(BaseUseCase):
    def __init__(
            self,
            payload: BaseModel,
            id: int,
            repository: ICRUDRepository,
            schema: BaseModel,
    ):
        super().__init__(payload, repository, schema)
        self._id = id

    async def _validate_email(self):
        user, _ = await self._repository.get_one_by(email=self._payload.email)
        if user and user.id != self._id:
            raise UseCaseException(MessagesEnum.EMAIL_ALREADY_EXIST.value, 400)

    async def _validate_id(self):
        if not await self._repository.get_one_by(id=self._id):
            raise UseCaseException(MessagesEnum.USER_NOT_FOUND.value, 400)

    async def execute(self):
        await self._validate_id()

        await self._validate_email()

        user_payload = self._payload.dict()
        user_payload["password"] = pbkdf2_sha256.hash(self._payload.password)

        updated = await self._repository.update(user_payload, self._id)
        if not updated:
            raise UseCaseException(MessagesEnum.USER_NOT_UPDATED.value, 400)
        result = await self._repository.get_by_id(self._id)

        return self._schema.from_orm(result)
