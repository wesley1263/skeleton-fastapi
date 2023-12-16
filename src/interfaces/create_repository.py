from abc import ABC, abstractmethod


class ICreateRepository(ABC):
    @abstractmethod
    async def create(self, **kwargs):
        pass
