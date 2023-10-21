from abc import ABC

from .base_repository import BaseRepository
from .create_repository import CreateRepository
from .delete_repository import DeleteRepository
from .retrieve_all_repository import RetrieveAllRepository
from .retrieve_one_by_repository import RetrieveOneByRepository
from .update_repository import UpdateRepository


class CRUDRepository(
    CreateRepository,
    UpdateRepository,
    RetrieveAllRepository,
    RetrieveOneByRepository,
    DeleteRepository,
    ABC,
):
    pass
