import pytest
from fastapi import status

END_POINT = "/users/"


def test_router_get_users_should_be_return_200_when_get_all_users(
    test_app_with_db, access_token
):
    response = test_app_with_db.get(END_POINT, headers=access_token)
    assert response.status_code == status.HTTP_200_OK


def test_router_user_create_should_be_return_201_when_post_user(
    test_app_with_db, user_post_fake_dict, access_token
):
    response = test_app_with_db.post(
        END_POINT, json=user_post_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_router_user_create_should_be_return_400_when_post_user(
    test_app_with_db, user_post_fake_dict, access_token
):
    response = test_app_with_db.post(
        END_POINT, json=user_post_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.fixture
def user_created(test_app_with_db, user_post_fake_dict, access_token):
    user_post_fake_dict["email"] = "email2@example.com"
    created = test_app_with_db.post(
        END_POINT, json=user_post_fake_dict, headers=access_token
    )
    return created.json()


def test_router_get_user_should_be_return_200_when_post_user(
    test_app_with_db, user_created, access_token
):
    response = test_app_with_db.get(
        f"{END_POINT}{user_created.get('id')}", headers=access_token
    )

    assert response.status_code == status.HTTP_200_OK


def test_router_get_user_by_email_should_be_return_200_when_post_user(
    test_app_with_db, user_created, access_token
):
    users = test_app_with_db.get(END_POINT, headers=access_token)
    email = users.json().get("items")[0].get("email")

    response = test_app_with_db.get(f"{END_POINT}email/{email}", headers=access_token)

    assert response.status_code == status.HTTP_200_OK


def test_router_put_user_should_be_return_200_when_payload_valid(
    test_app_with_db, user_put_fake_dict, access_token
):
    users = test_app_with_db.get(END_POINT, headers=access_token)
    payload = users.json().get("items")[0]

    payload["name"] = user_put_fake_dict["name"]
    payload["password"] = user_put_fake_dict["password"]
    payload["is_active"] = user_put_fake_dict["is_active"]

    response = test_app_with_db.put(
        f"{END_POINT}{payload.get('id')}", json=payload, headers=access_token
    )

    assert response.status_code == status.HTTP_200_OK


def test_login_user_should_be_return_400_when_payload_invalid(
    test_app_with_db, user_login_fake_dict, access_token
):
    response = test_app_with_db.post(
        f"{END_POINT}login", json=user_login_fake_dict, headers=access_token
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
