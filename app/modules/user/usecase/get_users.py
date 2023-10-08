from app.interfaces.repository_interface import RepositoryInterface

from .. import schema


class GetUsersUseCase:
    def __init__(self, repository: RepositoryInterface):
        self._repository = repository

    async def _serializer(self, user):
        return schema.GetUserSchema.from_orm(user)

    async def execute(self):
        users = await self._repository.get_all()
        return [await self._serializer(user) for user in users]
