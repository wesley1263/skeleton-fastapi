import pytest
from starlette.testclient import TestClient
from tortoise.contrib.starlette import register_tortoise

from app.config.settings import get_settings
from app.main import create_app

setting = get_settings()
setting.TESTING = True
setting.DB_URL = setting.DB_TEST_URL
app = create_app()


@pytest.fixture(scope="module")
def test_app():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    register_tortoise(
        app,
        db_url=setting.DB_TEST_URL,
        modules={"models": setting.ENTITIES},
        generate_schemas=True,
    )
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
