from abc import ABC

from loguru import logger
from tortoise.exceptions import BaseORMException

from app.abstracts.base_repository import BaseRepository
from app.interfaces.delete_repository import IDeleteRepository


class DeleteRepository(BaseRepository, IDeleteRepository, ABC):
    async def delete(self, id: int) -> bool:
        try:
            await self._entity.filter(id=id).delete()
            return True
        except BaseORMException as err:
            logger.critical(f"Error when try delete one entity: {str(err)}")
            return False
