from decouple import config
from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel

from src.interfaces.crud_repository import ICRUDRepository
from src.modules.user.schema import PostUserSchema


class CreateUserAdminUseCase:
    def __init__(self, repository: ICRUDRepository, schema: BaseModel):
        self._repository = repository
        self._create_admin_user = config("CREATE_ADMIN", default=False, cast=bool)
        self._schema = schema

    async def _validate(self):
        _email_admin = config("EMAIL_ADMIN")
        if self._create_admin_user and not await self._repository.get_one_by(
            email=_email_admin
        ):
            return self._schema(
                email=config("EMAIL_ADMIN"),
                name=config("NAME_ADMIN"),
                password=pbkdf2_sha256.hash(config("PASSWORD_ADMIN")),
                is_active=True,
            ).dict()
        return None

    async def execute(self):
        user_dict = await self._validate()
        if user_dict:
            await self._repository.create(user_dict)
