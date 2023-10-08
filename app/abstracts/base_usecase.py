from abc import ABCMeta, abstractmethod

from pydantic import BaseModel

from app.exceptions.usecase_exception import UseCaseException
from app.interfaces.repository_interface import RepositoryInterface


class BaseUseCase(metaclass=ABCMeta):
    def __init__(
        self,
        payload: BaseModel,
        repository: RepositoryInterface,
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
