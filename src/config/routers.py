from fastapi import FastAPI
from fastapi_pagination import add_pagination


async def init_routers(app: FastAPI):
    """
    This function is to load all routers in application.
    Here you can add routers from your modules.
    :param app:
    :return:
    """
    from src.modules.core import helthcheck_router
    from src.modules.user import router as user_router

    app.include_router(helthcheck_router.router)
    app.include_router(user_router.router, prefix="/users", tags=["User"])

    add_pagination(app)
