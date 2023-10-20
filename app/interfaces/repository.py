from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def get_by_id(self, id: int):
        pass

    @abstractmethod
    async def get_one_by(self, **kwargs):
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def create(self, **kwargs):
        pass

    @abstractmethod
    async def update(self, **kwa):
        pass
