from abc import ABC

from loguru import logger
from tortoise.exceptions import OperationalError
from tortoise.transactions import in_transaction
from app.abstracts.base_repository import BaseRepository
from app.interfaces.delete_repository import IDeleteRepository


class DeleteRepository(BaseRepository, IDeleteRepository, ABC):
    async def delete(self, id: int) -> bool:
        try:
            async with in_transaction() as conn:
                await self._entity.filter(id=id).using_db(conn).delete()
                return True
        except OperationalError as err:
            logger.critical(f"Error when try delete one entity: {str(err)}")
            return False
