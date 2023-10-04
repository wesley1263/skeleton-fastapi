from abc import ABCMeta, abstractmethod

from fastapi import HTTPException, status
from fastapi_camelcase import CamelModel
from tortoise.exceptions import BaseORMException
from tortoise.models import Model

from app.abstracts.base_repository import BaseRepository


class BaseUseCase(metaclass=ABCMeta):
    def __init__(
        self, payload: CamelModel, repository: BaseRepository, model: Model = None
    ):
        self._payload = payload
        self._repository = repository
        self._model = model

    async def _validate_db(self, detail_message: str, **kwargs):
        try:
            model = await self._repository.get_or_none(**kwargs)
            if not model:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=detail_message,
                )
            return model
        except BaseORMException as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err),
            )

    async def _already_exists_db(self, detail_message: str, **kwargs):
        try:
            model = await self._repository.get_or_none(**kwargs)
            if model:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=detail_message,
                )
        except BaseORMException as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err),
            )

    @abstractmethod
    async def execute(self):
        raise NotImplementedError()
