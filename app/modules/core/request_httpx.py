import httpx
from fastapi import HTTPException, status

from app.config.settings import get_settings
from app.interfaces.request_interface import RequestInterface

settings = get_settings()


class RequestHttpx(RequestInterface):
    def __init__(self):
        self._client = httpx.AsyncClient(timeout=httpx.Timeout(5.0))

    async def async_request(self, url: str, method: str, **kwargs):
        try:
            response = await self._client.request(method, url, **kwargs)
            return response
        except httpx.RequestError as e:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(e))

    async def async_get(self, url: str, **kwargs):
        response = await self._client.get(url, **kwargs)
        return response

    async def async_post(self, url: str, payload: dict, **kwargs):
        response = await self._client.post(url, data=payload, **kwargs)
        return response

    async def async_put(self, url: str, payload: dict, **kwargs):
        response = await self._client.put(url, data=payload, **kwargs)
        return response

    async def async_delete(self, url: str, **kwargs):
        response = await self._client.delete(url, **kwargs)
        return response

    @staticmethod
    def request(url: str, method: str, **kwargs):
        try:
            response = httpx.request(method, url, **kwargs)
            return response
        except httpx.RequestError as e:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(e))

    @staticmethod
    def get(url: str, **kwargs):
        response = httpx.get(url, **kwargs)
        return response

    @staticmethod
    def post(url: str, payload: dict, **kwargs):
        response = httpx.post(url, data=payload, **kwargs)
        return response

    @staticmethod
    def put(url: str, payload: dict, **kwargs):
        response = httpx.put(url, data=payload, **kwargs)
        return response

    @staticmethod
    def delete(url: str, **kwargs):
        response = httpx.delete(url, **kwargs)
        return response
