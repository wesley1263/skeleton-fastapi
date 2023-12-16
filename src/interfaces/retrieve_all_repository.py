from abc import ABC, abstractmethod


class IRetrieveAllRepository(ABC):
    @abstractmethod
    async def get_all(self):
        pass
