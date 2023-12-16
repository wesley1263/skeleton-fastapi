from abc import ABC, abstractmethod


class IUpdateRepository(ABC):
    @abstractmethod
    async def update(self, **kwargs):
        pass
