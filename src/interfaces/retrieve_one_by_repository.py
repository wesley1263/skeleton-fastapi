from abc import ABC, abstractmethod


class IRetrieveOneByRepository(ABC):
    @abstractmethod
    async def get_one_by(self, **kwargs):
        pass
