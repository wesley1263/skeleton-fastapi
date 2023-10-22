from abc import ABC

from loguru import logger
from tortoise.exceptions import OperationalError
from tortoise.transactions import in_transaction
from ..interfaces.create_repository import ICreateRepository
from .base_repository import BaseRepository


class UpdateRepository(BaseRepository, ICreateRepository, ABC):
    async def update(self, payload: dict, id: int) -> bool:
        try:
            async with in_transaction() as conn:
                await self._entity.filter(id=id).using_db(conn).update(**payload)
                return True
        except OperationalError as err:
            logger.critical(f"Error when try update entity: {str(err)}")
            return False
