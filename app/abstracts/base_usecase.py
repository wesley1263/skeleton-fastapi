from abc import abstractmethod, ABC

from pydantic import BaseModel

from app.exceptions.usecase import UseCaseException
from app.interfaces.repository import IRepository


class BaseUseCase(ABC):
    def __init__(
        self,
        payload: BaseModel,
        repository: IRepository,
        schema: BaseModel = None,
    ):
        self._payload = payload
        self._repository = repository
        self._schema = schema

    async def _validate_db(self, detail_message: str, **kwargs):
        try:
            model = await self._repository.get_one_by(**kwargs)
            if not model:
                raise UseCaseException(detail_message, 404)
            return model
        except Exception as err:
            raise UseCaseException(str(err), 500)

    async def _already_exists_db(self, detail_message: str, **kwargs):
        try:
            model = await self._repository.get_one_by(**kwargs)
            if model:
                raise UseCaseException(detail_message, 400)
        except Exception as err:
            raise UseCaseException(str(err), 500)

    @abstractmethod
    async def execute(self):
        raise NotImplementedError()
