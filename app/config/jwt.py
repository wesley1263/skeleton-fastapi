from decouple import config
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseSettings

from app.config.settings import get_settings

setting = get_settings()


class Setting(BaseSettings):
    authjwt_secret_key: str = config("SECRET_KEY")


async def exception_jwt(app: FastAPI):
    @app.exception_handler(AuthJWTException)
    def auth_jwt_exception_handler(_request: Request, exc: AuthJWTException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message},
        )


def get_settings_overide():
    return Setting(authjwt_secret_key=config("SECRET_KEY"))


async def init_jwt():
    @AuthJWT.load_config
    def get_setting_jwt():
        return get_settings_overide()
