from tortoise import Model

from src.modules.user.entity import UserEntity


def test_user_entity_should_return_valid_instance_when_valid_data_is_passed(
    user_fake_dict,
):
    user = UserEntity(**user_fake_dict)
    assert isinstance(user, Model)
    assert isinstance(user, UserEntity)


def test_user_entity_should_return_valid_fields_when_valid_data_is_passed(
    user_fake_dict,
):
    user = UserEntity(**user_fake_dict)

    assert isinstance(user.name, str)
    assert isinstance(user.email, str)
    assert isinstance(user.password, str)
    assert isinstance(user.is_active, bool)

    assert user.name == user_fake_dict["name"]
    assert user.email == user_fake_dict["email"]
    assert user.password == user_fake_dict["password"]
    assert user.__str__() == user.name
