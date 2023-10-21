from abc import ABC

from .create_repository import ICreateRepository
from .delete_repository import IDeleteRepository
from .retrieve_all_repository import IRetrieveAllRepository
from .retrieve_one_by_repository import IRetrieveOneByRepository
from .update_repository import IUpdateRepository


class ICRUDRepository(
    IRetrieveAllRepository,
    IRetrieveOneByRepository,
    ICreateRepository,
    IUpdateRepository,
    IDeleteRepository,
    ABC,
):
    pass
