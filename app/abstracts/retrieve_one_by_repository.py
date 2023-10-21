from abc import ABC

from loguru import logger
from pydantic import BaseModel
from tortoise.exceptions import OperationalError

from app.abstracts.base_repository import BaseRepository
from app.interfaces.retrieve_one_by_repository import IRetrieveOneByRepository


class RetrieveOneByRepository(BaseRepository, IRetrieveOneByRepository, ABC):
    async def get_one_by(self, **kwargs) -> [BaseModel, None]:
        try:
            _result = await self._entity.get_or_none(**kwargs)
            if not _result:
                return None
            return self._model.from_orm(_result)
        except OperationalError as err:
            logger.critical(f"Error when try get one entity: {str(err)}")
            return None
