from abc import ABC, abstractmethod

from pydantic import BaseModel

from app.exceptions.usecase import UseCaseException
from app.interfaces.crud_repository import ICRUDRepository


class BaseUseCase(ABC):
    """

    BaseUseCase

    Abstract base class for implementing use cases in the application.

    Attributes:
        _payload (BaseModel): The payload that the use case will operate on.
        _repository (ICRUDRepository): The repository interface used for data operations.
        _schema (BaseModel): The schema that defines the data structure of the payload.

    Methods:
        execute: Abstract method that needs to be implemented by subclasses.
    """
    def __init__(
            self,
            payload: BaseModel,
            repository: ICRUDRepository,
            schema: BaseModel = None,
    ):
        self._payload = payload
        self._repository = repository
        self._schema = schema

    @abstractmethod
    async def execute(self):
        raise NotImplementedError()
