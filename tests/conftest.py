import asyncio

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient
from tortoise.contrib.starlette import register_tortoise

from app.config.database import connect_to_database, run_migrate
from app.config.jwt import init_jwt
from app.config.middlewares import init_middlewares
from app.config.routers import init_routers
from app.config.settings import get_settings
from app.main import create_app

setting = get_settings()
setting.TESTING = True
setting.DB_URL = setting.DB_TEST_URL


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    run_configs(app)

    with TestClient(app) as test_client:
        yield test_client


def run_configs(app: FastAPI):
    init_middlewares(app)
    asyncio.run(init_routers(app))
    asyncio.run(init_jwt())
    asyncio.run(connect_to_database())
    asyncio.run(run_migrate())


@pytest.fixture(scope="module")
def test_app_with_db():
    app = create_app()
    run_configs(app)
    # register_tortoise(
    #     app,
    #     db_url=setting.DB_TEST_URL,
    #     modules={"models": setting.ENTITIES},
    #     generate_schemas=True,
    # )
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def access_token(test_app_with_db):
    test_app_with_db.post("/users/create-admin")
    response = test_app_with_db.post(
        "/users/login",
        json={"email": setting.EMAIL_ADMIN, "password": setting.PASSWORD_ADMIN},
    )

    payload = response.json()

    return {"Authorization": f"Bearer {payload.get('accessToken')}"}
