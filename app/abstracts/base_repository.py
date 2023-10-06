from typing import TypeVar

from tortoise.exceptions import BaseORMException

from app.interfaces.repository_interface import RepositoryInterface

T = TypeVar("T")


class BaseRepository(RepositoryInterface):
    def __init__(self, model: T):
        self.entity = model

    async def create(self, payload: dict):
        return await self.entity.create(**payload)

    async def update(self, payload: dict, id: int) -> bool:
        try:
            await self.entity.filter(id=id).update(**payload)
            return True
        except BaseORMException:
            return False

    async def get_all(self) -> list:
        return await self.entity.all()

    async def get_one_by(self, **kwargs) -> [dict, None]:
        return await self.entity.get_or_none(**kwargs)

    async def get_by_id(self, id: int) -> [dict, None]:
        return await self.entity.get_or_none(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.entity.filter(id=id).delete()
            return True
        except BaseORMException:
            return False
