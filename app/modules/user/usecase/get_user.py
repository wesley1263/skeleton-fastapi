from pydantic import BaseModel

from app.exceptions.usecase import UseCaseException
from app.interfaces.crud_repository import ICRUDRepository

from ..enums import UserEnum


class GetUserUseCase:
    def __init__(self, id: int, repository: ICRUDRepository, schema: BaseModel):
        self._id = id
        self._repository = repository
        self._schema = schema

    async def _validate(self):
        user = await self._repository.get_by_id(self._id)
        if not user:
            raise UseCaseException(UserEnum.USER_NOT_FOUND.value, 404)
        return user

    async def execute(self) -> BaseModel:
        user = await self._validate()
        return self._schema(**user.dict())
