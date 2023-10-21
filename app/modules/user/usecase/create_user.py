from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel

from app.abstracts.base_usecase import BaseUseCase
from app.exceptions.usecase import UseCaseException
from app.interfaces.repository import IRepository

from ..enums import UserEnum


class CreateUserUseCase(BaseUseCase):
    def __init__(self, payload: BaseModel, repository: IRepository, schema: BaseModel):
        super().__init__(payload, repository, schema)

    async def _validate_email(self):
        user = await self._repository.get_one_by(email=self._payload.email)
        if user:
            raise UseCaseException(UserEnum.EMAIL_ALREADY_EXIST.value, 400)

    async def execute(self):
        await self._validate_email()

        self._payload.password = pbkdf2_sha256.hash(self._payload.password)
        user = await self._repository.create(self._payload.dict())
        if not user:
            raise UseCaseException(UserEnum.ERROR_CREATE_USER.value, 500)
        return self._schema(**user.dict())
