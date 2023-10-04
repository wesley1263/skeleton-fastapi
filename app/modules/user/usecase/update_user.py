from fastapi import HTTPException
from passlib.hash import pbkdf2_sha256

from app.abstracts.base_repository import BaseRepository
from app.modules.core.messages_enum import MessagesEnum
from app.modules.user import schema


class UpdateUserUseCase:
    def __init__(
        self, payload: schema.UpdateUserSchema, id: int, repository: BaseRepository
    ):
        self._id = id
        self._payload = payload
        self._repository = repository

    async def _validate(self):
        user = await self._repository.get_by_id(self._id)
        if not user:
            raise HTTPException(status_code=404, detail=MessagesEnum.USER_NOT_FOUND)

    async def _validate_email(self):
        user = await self._repository.get_by_email(self._payload.email)
        if user and user.id != self._id:
            raise HTTPException(
                status_code=400, detail=MessagesEnum.EMAIL_ALREADY_EXIST
            )

    async def execute(self):
        await self._validate()
        await self._validate_email()

        user_payload = self._payload.dict()
        user_payload["password"] = pbkdf2_sha256.hash(self._payload.password)

        updated = await self._repository.update(user_payload, self._id)
        if not updated:
            raise HTTPException(status_code=400, detail=MessagesEnum.USER_NOT_UPDATED)
        result = await self._repository.get_by_id(self._id)

        return schema.GetUserSchema.from_orm(result)
