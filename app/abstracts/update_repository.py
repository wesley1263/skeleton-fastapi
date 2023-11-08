from abc import ABC

from loguru import logger
from tortoise.exceptions import OperationalError
from tortoise.transactions import in_transaction
from ..interfaces.create_repository import ICreateRepository
from .base_repository import BaseRepository


class UpdateRepository(BaseRepository, ICreateRepository, ABC):
    """

    UpdateRepository Class

    This class represents a repository for updating entities in a database. It extends the BaseRepository class and implements the ICreateRepository interface.

    Methods:
    - update(payload: dict, id: int) -> bool: Updates an entity in the database with the specified payload and ID.

    """
    async def update(self, payload: dict, id: int) -> bool:
        try:
            async with in_transaction() as conn:
                await self._entity.filter(id=id).using_db(conn).update(**payload)
                return True
        except OperationalError as err:
            logger.critical(f"Error when try update entity: {str(err)}")
            return False
