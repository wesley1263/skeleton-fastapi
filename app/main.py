from loguru import logger

from app.config.apm import init_apm
from app.config.bootstrap import create_app
from app.config.db import close_connection_database, connect_to_database
from app.config.jwt import exception_jwt, init_jwt
from app.config.middlewares import init_middlewares
from app.config.routers import init_routers

app = create_app()

init_middlewares(app)
init_apm(app)


@app.on_event("startup")
async def startup_db():
    logger.info("Starting up database...")
    await connect_to_database()


@app.on_event("startup")
async def startup_routers():
    logger.info("Starting up routers...")
    await init_routers(app)


@app.on_event("startup")
async def startup_jwt():
    logger.info("Starting up JWT...")
    await init_jwt()


@app.on_event("startup")
async def startup_exception_jwt():
    logger.info("Starting up exceptions JWT...")
    await exception_jwt(app)


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    await close_connection_database()
