from loguru import logger

from app.config.bootstrap import create_app
from app.config.database import close_connection_database, connect_to_database
from app.config.jwt import exception_jwt, init_jwt
from app.config.middlewares import init_middlewares
from app.config.routers import init_routers

app = create_app()

init_middlewares(app)


@app.on_event("startup")
async def startup_app():
    logger.info("Starting up database...")
    await connect_to_database()
    logger.info("Starting up routers...")
    await init_routers(app)
    logger.info("Starting up JWT...")
    await init_jwt()
    logger.info("Starting up exceptions JWT...")
    await exception_jwt(app)


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    await close_connection_database()
