from abc import ABC

from loguru import logger
from pydantic import BaseModel
from tortoise.exceptions import OperationalError
from tortoise.transactions import in_transaction

from app.abstracts.base_repository import BaseRepository
from app.interfaces.create_repository import ICreateRepository


class CreateRepository(BaseRepository, ICreateRepository, ABC):
    async def create(self, payload: dict) -> [BaseModel, None]:
        try:
            async with in_transaction() as conn:
                _result = await self._entity.create(**payload, using_db=conn)
                if not _result:
                    return None
                return self._model.from_orm(_result)
        except OperationalError as err:
            logger.critical(f"Error when try create entity: {str(err)}")
            return None
