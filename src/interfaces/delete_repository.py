from abc import ABC, abstractmethod


class IDeleteRepository(ABC):
    @abstractmethod
    async def delete(self, **kwargs):
        pass
