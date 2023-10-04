from fastapi import HTTPException
from fastapi_jwt_auth import AuthJWT
from passlib.hash import pbkdf2_sha256

from app.abstracts.base_repository import BaseRepository
from app.modules.core.messages_enum import MessagesEnum
from app.modules.user import schema


class LoginUseCase:
    def __init__(
        self,
        payload: schema.LoginUserSchema,
        authorize: AuthJWT,
        repository: BaseRepository,
    ):
        self._payload = payload
        self._repository = repository
        self._authorize = authorize

    async def _validate(self):
        user = await self._repository.get_by_email(self._payload.email)
        if not user:
            raise HTTPException(status_code=404, detail=MessagesEnum.USER_NOT_FOUND)
        return user

    async def _serializer(self, user):
        access_token = self._authorize.create_access_token(subject=user.email)
        return {
            "email": user.email,
            "access_token": access_token,
        }

    async def execute(self):
        user = await self._validate()
        if not pbkdf2_sha256.verify(self._payload.password, user.password):
            raise HTTPException(status_code=400, detail=MessagesEnum.INVALID_PASSWORD)
        user_serialized = await self._serializer(user)
        return schema.JWTUserSchema(**user_serialized)
