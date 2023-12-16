from fastapi_camelcase import CamelModel
from pydantic import BaseModel

from src.modules.user import schema


def test_user_schema_should_return_valid_instance_when_valid_data_is_passed(
    user_fake_dict,
):
    user_schema = schema.GetUserSchema(**user_fake_dict)

    assert isinstance(user_schema, schema.GetUserSchema)
    assert isinstance(user_schema, CamelModel)
    assert isinstance(user_schema, BaseModel)


def test_user_schema_should_return_valid_instance_fields_when_valid_data_is_passed(
    user_fake_dict,
):
    user_schema = schema.GetUserSchema(**user_fake_dict)

    assert isinstance(user_schema.id, int)
    assert isinstance(user_schema.email, str)
    assert isinstance(user_schema.name, str)
    assert isinstance(user_schema.is_active, bool)

    assert user_schema.id == user_fake_dict["id"]
    assert user_schema.email == user_fake_dict["email"]
    assert user_schema.name == user_fake_dict["name"]


def test_user_post_schema_should_return_valid_instance_when_valid_data_is_passed(
    user_post_fake_dict,
):
    user_schema = schema.PostUserSchema(**user_post_fake_dict)

    assert isinstance(user_schema, schema.PostUserSchema)
    assert isinstance(user_schema, CamelModel)
    assert isinstance(user_schema, BaseModel)
