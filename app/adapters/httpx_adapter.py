import httpx

from app.abstracts.adapter_exception import AdapterException
from app.config.settings import get_settings
from app.interfaces.request import IRequest

settings = get_settings()


class HttpxAdapter(IRequest):
    def __init__(self):
        self._client = httpx.AsyncClient(timeout=httpx.Timeout(5.0))

    async def async_request(self, url: str, method: str, **kwargs):
        try:
            response = await self._client.request(method, url, **kwargs)
            return response
        except httpx.RequestError as err:
            raise AdapterException(str(err))

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
        except httpx.RequestError as err:
            raise AdapterException(str(err))

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
