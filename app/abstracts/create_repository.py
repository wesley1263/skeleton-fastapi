from abc import ABC

from loguru import logger
from pydantic import BaseModel
from tortoise.exceptions import BaseORMException

from app.abstracts.base_repository import BaseRepository
from app.interfaces.create_repository import ICreateRepository


class CreateRepository(BaseRepository, ICreateRepository, ABC):
    async def create(self, payload: dict) -> [BaseModel, None]:
        try:
            _result = await self._entity.create(**payload)
            if not _result:
                return None
            return self._model.from_orm(_result)
        except BaseORMException as err:
            logger.critical(f"Error when try create entity: {str(err)}")
            return None
