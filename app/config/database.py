import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.starlette import register_tortoise

from .settings import get_settings

settings = get_settings()

log = logging.getLogger("uvicorn")

""" This config is for generate migrations.bkp by aerich """
TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": settings.ENTITIES,
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI):
    """This function is to configuration database credentials"""
    register_tortoise(
        app=app,
        db_url=settings.DB_URL if not settings.TESTING else settings.DB_TEST_URL,
        generate_schemas=settings.GENERATE_SCHEMAS,
        modules={"models": settings.ENTITIES},
    )


async def connect_to_database() -> None:
    log.info("Initialize Tortoise...")
    await Tortoise.init(
        db_url=settings.DB_URL,
        modules={"models": settings.ENTITIES},
    )


async def run_migrate():
    result = os.popen("aerich upgrade").read()
    log.info(f"Result migrate: {result}")


async def close_connection_database() -> None:
    log.info("Closing Tortoise...")
    await Tortoise.close_connections()
