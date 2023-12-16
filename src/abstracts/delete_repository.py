from abc import ABC

from loguru import logger
from tortoise.exceptions import OperationalError
from tortoise.transactions import in_transaction

from src.abstracts.base_repository import BaseRepository
from src.interfaces.delete_repository import IDeleteRepository


class DeleteRepository(BaseRepository, IDeleteRepository, ABC):
    """

    This class `DeleteRepository` is a concrete implementation of the `BaseRepository` and `IDeleteRepository` interfaces. It provides the functionality to delete an entity from the database.

    Methods:
        - `delete`: Deletes an entity from the database based on the provided ID.

    """

    async def delete(self, id: int) -> bool:
        try:
            async with in_transaction() as conn:
                await self._entity.filter(id=id).using_db(conn).delete()
                return True
        except OperationalError as err:
            logger.critical(f"Error when try delete one entity: {str(err)}")
            return False
