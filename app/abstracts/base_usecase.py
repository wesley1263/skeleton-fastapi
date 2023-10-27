from abc import ABC, abstractmethod

from pydantic import BaseModel

from app.exceptions.usecase import UseCaseException
from app.interfaces.crud_repository import ICRUDRepository


class BaseUseCase(ABC):
    def __init__(
        self,
        payload: BaseModel,
        repository: ICRUDRepository,
        schema: BaseModel = None,
    ):
        self._payload = payload
        self._repository = repository
        self._schema = schema

    async def _validate_db(self, detail_message: str, **kwargs):
        _domain, _ = await self._repository.get_one_by(**kwargs)
        if not _domain:
            raise UseCaseException(detail_message, 404)
        return _domain

    async def _already_exists_db(self, detail_message: str, **kwargs):
        try:
            _domain, _ = await self._repository.get_one_by(**kwargs)
            if _domain:
                raise UseCaseException(detail_message, 400)
        except Exception as err:
            raise UseCaseException(str(err), 500)

    @abstractmethod
    async def execute(self):
        raise NotImplementedError()
