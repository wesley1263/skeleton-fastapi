from fastapi import HTTPException

from app.abstracts.base_repository import BaseRepository
from app.modules.core.messages_enum import MessagesEnum
from app.modules.user import schema


class GetUserByEmailUseCase:
    def __init__(self, email: str, repository: BaseRepository):
        self._email = email
        self._repository = repository

    async def _validate(self):
        user = await self._repository.get_by_email(self._email)
        if not user:
            raise HTTPException(status_code=404, detail=MessagesEnum.USER_NOT_FOUND)
        return user

    async def execute(self):
        user = await self._validate()
        return schema.GetUserSchema.from_orm(user)
