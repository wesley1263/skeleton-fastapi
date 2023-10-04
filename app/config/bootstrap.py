from fastapi import FastAPI
from loguru import logger

from app.config.settings import get_settings

setting = get_settings()

logger.remove(0)


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(
        title=setting.APP_NAME,
        version=setting.APP_VERSION,
        description=setting.APP_DESCRIPTION,
        root_path=setting.ROOT_PATH,
    )

    return application
