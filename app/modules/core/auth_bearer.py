from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_jwt_auth import AuthJWT

from app.config.settings import get_settings

settings = get_settings()


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request, authorization: AuthJWT = Depends()):
        if not settings.TESTING:
            credentials: HTTPAuthorizationCredentials = await super(
                JWTBearer, self
            ).__call__(request)
            authorization.jwt_required()
            return credentials
