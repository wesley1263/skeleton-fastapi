from fastapi import HTTPException, status

from app.abstracts.base_repository import BaseRepository
from app.modules.core.messages_enum import MessagesEnum

from .. import schema


class GetUserUseCase:
    def __init__(self, id: int, repository: BaseRepository):
        self._id = id
        self._repository = repository

    async def _validate(self):
        user = await self._repository.get_by_id(self._id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=MessagesEnum.USER_NOT_FOUND,
            )
        return user

    async def execute(self):
        user = await self._validate()
        return schema.GetUserSchema.from_orm(user)
