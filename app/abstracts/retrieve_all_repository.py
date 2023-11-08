from abc import ABC
from typing import List, Optional

from loguru import logger
from pydantic import BaseModel
from tortoise.exceptions import OperationalError

from ..interfaces.retrieve_all_repository import IRetrieveAllRepository
from .base_repository import BaseRepository


class RetrieveAllRepository(BaseRepository, IRetrieveAllRepository, ABC):
    """

    This class is an implementation of the `IRetrieveAllRepository` interface. It inherits from the `BaseRepository` class.

    Methods:
        - get_all(): Retrieves all entities from the database.

    Attributes:
        - _entity: Database entity to retrieve data from.
        - _model: Pydantic model to convert retrieved entities into.

    """
    async def get_all(self) -> (List[BaseModel], []):
        try:
            _result = await self._entity.all()
            if not _result:
                return []
            return [self._model.from_orm(entity) for entity in _result]
        except OperationalError as err:
            logger.critical(f"Error when try retrieve list from entity: {str(err)}")
            return []
