from pydantic import BaseModel

from src.interfaces.crud_repository import ICRUDRepository

from .. import schema


class GetUsersUseCase:
    def __init__(self, repository: ICRUDRepository, schema: BaseModel):
        self._repository = repository
        self._schema = schema

    async def _serializer(self, user) -> BaseModel:
        return self._schema(**user.dict())

    async def execute(self):
        users = await self._repository.get_all()
        if not len(users):
            return []
        return [await self._serializer(user) for user in users]
