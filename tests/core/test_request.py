import httpx
from fastapi import status

from app.adapters.httpx_adapter import HttpxAdapter

URL_GOOGLE = "https://www.google.com"


def test_get_request_httpx():
    response = HttpxAdapter.get(URL_GOOGLE)
    assert response.status_code == status.HTTP_200_OK


async def test_get_request_httpx_async():
    response = await HttpxAdapter().async_get(URL_GOOGLE)
    assert response.status_code == status.HTTP_200_OK


async def test_request_httpx_async():
    response = await HttpxAdapter().async_request(URL_GOOGLE, "GET")
    assert response.status_code == status.HTTP_200_OK


def test_request_httpx():
    response = HttpxAdapter.request(URL_GOOGLE, "GET", params={"q": "test"})
    assert response.status_code == status.HTTP_200_OK


def test_post_request_httpx(monkeypatch):
    def mock_post(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(HttpxAdapter, "post", mock_post)
    response = HttpxAdapter.post(URL_GOOGLE, payload={"q": "test"})

    assert response.status_code == status.HTTP_200_OK


async def test_post_request_httpx_async(monkeypatch):
    async def mock_post(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(HttpxAdapter, "async_post", mock_post)
    response = await HttpxAdapter().async_post(URL_GOOGLE, payload={"q": "test"})

    assert response.status_code == status.HTTP_200_OK


def test_put_request_httpx(monkeypatch):
    def mock_put(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(HttpxAdapter, "put", mock_put)
    response = HttpxAdapter.put(URL_GOOGLE, payload={"q": "test"})

    assert response.status_code == status.HTTP_200_OK


async def test_put_request_httpx_async(monkeypatch):
    async def mock_put(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(HttpxAdapter, "async_put", mock_put)
    response = await HttpxAdapter().async_put(URL_GOOGLE, payload={"q": "test"})

    assert response.status_code == status.HTTP_200_OK


def test_delete_request_httpx(monkeypatch):
    def mock_delete(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(HttpxAdapter, "delete", mock_delete)
    response = HttpxAdapter.delete(URL_GOOGLE)

    assert response.status_code == status.HTTP_200_OK


async def test_delete_request_httpx_async(monkeypatch):
    async def mock_delete(*args, **kwargs):
        return httpx.Response(200)

    monkeypatch.setattr(HttpxAdapter, "async_delete", mock_delete)
    response = await HttpxAdapter().async_delete(URL_GOOGLE)

    assert response.status_code == status.HTTP_200_OK
