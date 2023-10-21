from abc import ABC

from loguru import logger
from tortoise.exceptions import BaseORMException

from ..interfaces.create_repository import ICreateRepository
from .base_repository import BaseRepository


class UpdateRepository(BaseRepository, ICreateRepository, ABC):
    async def update(self, payload: dict, id: int) -> bool:
        try:
            await self._entity.filter(id=id).update(**payload)
            return True
        except BaseORMException as err:
            logger.critical(f"Error when try update entity: {str(err)}")
            return False
