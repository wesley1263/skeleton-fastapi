from abc import ABC

from loguru import logger
from pydantic import BaseModel
from tortoise import Model
from tortoise.exceptions import OperationalError

from app.abstracts.base_repository import BaseRepository
from app.interfaces.retrieve_one_by_repository import IRetrieveOneByRepository


class RetrieveOneByRepository(BaseRepository, IRetrieveOneByRepository, ABC):
    async def get_one_by(self, **kwargs) -> [(BaseModel, Model), (None, None)]:
        try:
            _entity_object = await self._entity.get_or_none(**kwargs)
            if not _entity_object:
                return None, None
            _model_object = self._model.from_orm(_entity_object)
            return _model_object, _entity_object
        except OperationalError as err:
            logger.critical(f"Error when try get one entity: {str(err)}")
            return None, None
