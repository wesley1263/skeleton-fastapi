import pytest
from faker import Factory

faker = Factory.create("pt_BR")


@pytest.fixture(scope="session")
def user_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
    }


@pytest.fixture(scope="session")
def user_post_fake_dict():
    return {
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "is_active": True,
    }


@pytest.fixture(scope="session")
def user_put_fake_dict():
    return {
        "name": faker.name(),
        "password": faker.password(),
        "is_active": False,
    }


@pytest.fixture(scope="session")
def user_login_fake_dict():
    return {
        "email": faker.email(),
        "password": faker.password(),
    }
