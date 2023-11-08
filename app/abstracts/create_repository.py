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
    """
    Class CreateRepository

    This class provides the implementation for creating entities in the database.

    Attributes:
        - Inherits from BaseRepository and ICreateRepository.
        - Uses the loguru library for logging.
        - Requires the pydantic BaseModel and the tortoise Model.
        - Handles OperationalError exceptions using tortoise transactions.

    Methods:
        - create(payload: dict) -> ([BaseModel, Model], [None, None])
            Accepts a dictionary of payload data.
            Creates a new entity in the database using the payload data.
            Returns a tuple containing the created model object and entity object, or None if creation fails.
            Logs critical errors if encountered during the creation process.
    """
    async def create(self, payload: dict) -> ([BaseModel, Model], [None, None]):
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
