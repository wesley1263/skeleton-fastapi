from loguru import logger
from tortoise import Tortoise

from .settings import get_settings

settings = get_settings()

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
    logger.info("Initialize Tortoise...")
    await Tortoise.init(config=TORTOISE_ORM)


async def close_connection_database() -> None:
    logger.info("Closing Tortoise...")
    await Tortoise.close_connections()
