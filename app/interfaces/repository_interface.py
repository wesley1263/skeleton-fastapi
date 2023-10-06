from abc import ABCMeta, abstractmethod


class RepositoryInterface(metaclass=ABCMeta):
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
