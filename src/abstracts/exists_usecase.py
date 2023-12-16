from abc import ABC

from ..exceptions.usecase import UseCaseException
from .base_usecase import BaseUseCase


class ExistsUsecase(BaseUseCase, ABC):
    """This class is a base class for usecases that check if an entity exists in the database."""

    async def _already_exists(self, detail_message: str, **kwargs):
        """
        Check if a domain object already exists based on given query parameters.

        :param detail_message: A detail message to be included in the UseCaseException if the object already exists.
        :param kwargs: Query parameters to use when checking for existence of the domain object.
        :raises UseCaseException: If the domain object already exists, a UseCaseException with the detail_message and error code 400 will be raised. If there is any other exception, a UseCaseException with the error message and error code 500 will be raised.
        """
        try:
            _domain, _ = await self._repository.get_one_by(**kwargs)
            if _domain:
                raise UseCaseException(detail_message, 400)
        except Exception as err:
            raise UseCaseException(str(err), 500)
