import httpx
from fastapi import status

from app.modules.core.request_httpx import RequestHttpx

URL_GOOGLE = "https://www.google.com"


def test_get_request_httpx():
    response = RequestHttpx.get(URL_GOOGLE)
    assert response.status_code == status.HTTP_200_OK


async def test_get_request_httpx_async():
    response = await RequestHttpx().async_get(URL_GOOGLE)
    assert response.status_code == status.HTTP_200_OK


async def test_request_httpx_async():
    response = await RequestHttpx().async_request(URL_GOOGLE, "GET")
    assert response.status_code == status.HTTP_200_OK


def test_request_httpx():
    response = RequestHttpx.request(URL_GOOGLE, "GET", params={"q": "test"})
    assert response.status_code == status.HTTP_200_OK


def test_post_request_httpx(monkeypatch):
    def mock_post(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(RequestHttpx, "post", mock_post)
    response = RequestHttpx.post(URL_GOOGLE, payload={"q": "test"})

    assert response.status_code == status.HTTP_200_OK


async def test_post_request_httpx_async(monkeypatch):
    async def mock_post(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(RequestHttpx, "async_post", mock_post)
    response = await RequestHttpx().async_post(URL_GOOGLE, payload={"q": "test"})

    assert response.status_code == status.HTTP_200_OK


def test_put_request_httpx(monkeypatch):
    def mock_put(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(RequestHttpx, "put", mock_put)
    response = RequestHttpx.put(URL_GOOGLE, payload={"q": "test"})

    assert response.status_code == status.HTTP_200_OK


async def test_put_request_httpx_async(monkeypatch):
    async def mock_put(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(RequestHttpx, "async_put", mock_put)
    response = await RequestHttpx().async_put(URL_GOOGLE, payload={"q": "test"})

    assert response.status_code == status.HTTP_200_OK


def test_delete_request_httpx(monkeypatch):
    def mock_delete(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(RequestHttpx, "delete", mock_delete)
    response = RequestHttpx.delete(URL_GOOGLE)

    assert response.status_code == status.HTTP_200_OK


async def test_delete_request_httpx_async(monkeypatch):
    async def mock_delete(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(RequestHttpx, "async_delete", mock_delete)
    response = await RequestHttpx().async_delete(URL_GOOGLE)

    assert response.status_code == status.HTTP_200_OK
