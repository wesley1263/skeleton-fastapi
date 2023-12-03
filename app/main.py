from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from app.config.database import close_connection_database, connect_to_database, init_db
from app.config.jwt import exception_jwt, init_jwt
from app.config.middlewares import init_middlewares
from app.config.routers import init_routers
from app.config.settings import get_settings

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up database")
    await connect_to_database()
    logger.info("Starting up routers")
    await init_routers(app)
    logger.info("Starting up JWT")
    await init_jwt()
    logger.info("Starting up exceptions JWT")
    await exception_jwt(app)

    yield

    logger.info("Shutting down...")
    await close_connection_database()


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        root_path=settings.ROOT_PATH,
        lifespan=lifespan,
    )

    return application


app = create_app()

init_middlewares(app)
logger.info("Init midlewares")
