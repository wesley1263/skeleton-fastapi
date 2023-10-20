from abc import ABC
from typing import List, Optional

from loguru import logger
from pydantic import BaseModel
from tortoise import Model
from tortoise.exceptions import BaseORMException

from app.interfaces.repository import IRepository


class BaseTortoiseRepository(IRepository, ABC):
    def __init__(self, model: BaseModel, entity: Model):
        self._entity = entity
        self._model = model

    async def create(self, payload: dict) -> [BaseModel, None]:
        try:
            _result = await self._entity.create(**payload)
            if not _result:
                return None
            return self._model.from_orm(_result)
        except BaseORMException as err:
            logger.critical(f"Error when try create entity: {str(err)}")
            return None

    async def update(self, payload: dict, id: int) -> bool:
        try:
            await self._entity.filter(id=id).update(**payload)
            return True
        except BaseORMException as err:
            logger.critical(f"Error when try update entity: {str(err)}")
            return False

    async def get_all(self) -> List[Optional[BaseModel]]:
        try:
            _result = await self._entity.all()
            if not _result:
                return []
            return [self._model.from_orm(entity) for entity in _result]
        except BaseORMException as err:
            logger.critical(f"Error when try retrieve list from entity: {str(err)}")
            return []

    async def get_one_by(self, **kwargs) -> [BaseModel, None]:
        try:
            _result = await self._entity.get_or_none(**kwargs)
            if not _result:
                return None
            return self._model.from_orm(_result)
        except BaseORMException as err:
            logger.critical(f"Error when try get one entity: {str(err)}")
            return None

    async def get_by_id(self, id: int) -> [BaseModel, None]:
        try:
            _result = await self._entity.get_or_none(id=id)
            if not _result:
                return None
            return self._model.from_orm(_result)
        except BaseORMException as err:
            logger.critical(f"Error when try get one entity: {str(err)}")
            return None

    async def delete(self, id: int) -> bool:
        try:
            await self._entity.filter(id=id).delete()
            return True
        except BaseORMException as err:
            logger.critical(f"Error when try delete one entity: {str(err)}")
            return False
