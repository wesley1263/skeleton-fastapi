from abc import ABC
from typing import Optional

from loguru import logger
from pydantic import BaseModel
from tortoise import Model
from tortoise.exceptions import OperationalError
from tortoise.transactions import in_transaction

from app.abstracts.base_repository import BaseRepository
from app.interfaces.create_repository import ICreateRepository


class CreateRepository(BaseRepository, ICreateRepository, ABC):
    async def create(self, payload: dict) -> ([BaseModel, Model], [None, None]):
        """ This method is using to create entity in database and parse to object domain"""
        try:
            async with in_transaction() as conn:
                _entity_object = await self._entity.create(**payload, using_db=conn)
                if not _entity_object:
                    return None, None
                _model_object = self._model.from_orm(_entity_object)
                return _model_object, _entity_object
        except OperationalError as err:
            logger.critical(f"Error when try create entity: {str(err)}")
            return None, None
