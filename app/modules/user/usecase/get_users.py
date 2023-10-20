from pydantic import BaseModel

from app.interfaces.repository import IRepository

from .. import schema


class GetUsersUseCase:
    def __init__(self, repository: IRepository, schema: BaseModel):
        self._repository = repository
        self._schema = schema

    async def _serializer(self, user) -> BaseModel:
        return self._schema(**user.dict())

    async def execute(self):
        users = await self._repository.get_all()
        return [await self._serializer(user) for user in users]
