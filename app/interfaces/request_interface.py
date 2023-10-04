from abc import ABC, abstractmethod


class RequestInterface(ABC):
    @abstractmethod
    def request(self, url: str, method: str, **kwargs):
        pass

    @abstractmethod
    def get(self, url: str, **kwargs):
        pass

    @abstractmethod
    def post(self, url: str, data: dict, **kwargs):
        pass

    @abstractmethod
    def put(self, url: str, data: dict, **kwargs):
        pass

    @abstractmethod
    def delete(self, url: str, **kwargs):
        pass
