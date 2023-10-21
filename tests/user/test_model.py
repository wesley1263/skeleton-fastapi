from pydantic import BaseModel

from app.modules.user.model import User


def test_user_model_should_return_valid_instance_when_valid_data_is_passed(
    user_fake_dict,
):
    user = User(**user_fake_dict)
    assert isinstance(user, BaseModel)


def test_user_model_should_return_valid_fields_when_valid_data_is_passed(
    user_fake_dict,
):
    user = User(**user_fake_dict)

    assert isinstance(user.name, str)
    assert isinstance(user.email, str)
    assert isinstance(user.password, str)

    assert user.name == user_fake_dict["name"]
    assert user.email == user_fake_dict["email"]
    assert user.password == user_fake_dict["password"]
