import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.starlette import register_tortoise

from .settings import get_settings

settings = get_settings()

log = logging.getLogger("uvicorn")

""" This config is for generate migrations by aerich """
TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": settings.ENTITIES,
            "default_connection": "default",
        },
    },
}


async def connect_to_database() -> None:
    log.info("Initialize Tortoise...")
    await Tortoise.init(
        db_url=settings.DB_URL,
        modules={"models": settings.ENTITIES},
    )


async def close_connection_database() -> None:
    log.info("Closing Tortoise...")
    await Tortoise.close_connections()
