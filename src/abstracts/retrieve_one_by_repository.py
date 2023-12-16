from abc import ABC

from loguru import logger
from pydantic import BaseModel
from tortoise import Model
from tortoise.exceptions import OperationalError

from src.abstracts.base_repository import BaseRepository
from src.interfaces.retrieve_one_by_repository import IRetrieveOneByRepository


class RetrieveOneByRepository(BaseRepository, IRetrieveOneByRepository, ABC):
    """
    This class is a concrete implementation of the `BaseRepository` class and the `IRetrieveOneByRepository` interface. It provides a method to retrieve a single entity from the database based on the given parameters.

    Attributes:
        None

    Methods:
        get_one_by(**kwargs) -> Tuple[(BaseModel, Model), (None, None)]: This method retrieves a single entity from the database based on the given parameters.

            - **kwargs (dict): The keyword arguments specifying the parameters to filter the database query.

            Returns:
                - Tuple[(BaseModel, Model), (None, None)]: A tuple containing the retrieved entity as a `BaseModel` and `Model` object, or `(None, None)` if the entity does not exist.

                - If an error occurs during the retrieval process, the method will log a critical message and return `(None, None)`.
    """

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
