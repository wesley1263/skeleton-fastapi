from abc import ABC

from pydantic import BaseModel
from tortoise import Model


class BaseRepository(ABC):
    def __init__(self, model: BaseModel, entity: Model):
        self._entity = entity
        self._model = model
