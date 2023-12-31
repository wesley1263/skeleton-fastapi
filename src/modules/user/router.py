from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page, paginate
from fastapi_pagination.utils import disable_installed_extensions_check
from passlib.hash import pbkdf2_sha256
from tortoise.exceptions import OperationalError
from tortoise.transactions import in_transaction

from src.config.settings import get_settings
from src.exceptions.usecase import UseCaseException
from src.modules.core.auth_bearer import JWTBearer
from src.modules.core.logging import LoggingSkeleton
from src.modules.user import schema, usecase
from src.modules.user.repository import UserRepository

disable_installed_extensions_check()

router = APIRouter()

setting = get_settings()

user_repository: UserRepository = UserRepository()


@router.get(
    "/",
    description="Router to list all users registered",
    response_model=Page[schema.GetUserSchema],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer()), Depends(LoggingSkeleton())],
)
async def get_users():
    users = await usecase.GetUsersUseCase(
        user_repository, schema.GetUserSchema
    ).execute()
    return paginate(users)


@router.get(
    "/{id}",
    description="Router to one user by id",
    response_model=schema.GetUserSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_user(id: int):
    try:
        return await usecase.GetUserUseCase(
            id, user_repository, schema.GetUserSchema
        ).execute()
    except UseCaseException as err:
        raise HTTPException(detail=str(err), status_code=err.status_code)


@router.post(
    "/",
    description="This router is to create new user",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.GetUserSchema,
    dependencies=[Depends(JWTBearer())],
)
async def post_user(payload: schema.PostUserSchema):
    try:
        async with in_transaction():
            return await usecase.CreateUserUseCase(
                payload, user_repository, schema.GetUserSchema
            ).execute()
    except UseCaseException as err:
        raise HTTPException(detail=str(err), status_code=err.status_code)
    except OperationalError:
        raise HTTPException(detail="Error when try create user", status_code=500)


@router.get(
    "/email/{email}",
    description="This router is to get one user by email",
    status_code=status.HTTP_200_OK,
    response_model=schema.GetUserSchema,
    dependencies=[Depends(JWTBearer())],
)
async def get_user_by_email(email: str):
    try:
        return await usecase.GetUserByEmailUseCase(
            email, user_repository, schema.GetUserSchema
        ).execute()
    except UseCaseException as err:
        raise HTTPException(detail=str(err), status_code=err.status_code)


@router.put(
    "/{id}",
    description="This router is to update user",
    status_code=status.HTTP_200_OK,
    response_model=schema.GetUserSchema,
    dependencies=[Depends(JWTBearer())],
)
async def put_user(id: int, payload: schema.UpdateUserSchema):
    try:
        async with in_transaction():
            return await usecase.UpdateUserUseCase(
                payload, id, user_repository, schema.GetUserSchema
            ).execute()
    except UseCaseException as err:
        raise HTTPException(detail=str(err), status_code=err.status_code)
    except OperationalError:
        raise HTTPException(detail="Error when try update user", status_code=500)


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=schema.JWTUserSchema,
    description="This router is to login user",
)
async def login(payload: schema.LoginUserSchema, authorize: AuthJWT = Depends()):
    try:
        return await usecase.LoginUseCase(
            payload, user_repository, schema.JWTUserSchema, authorize, pbkdf2_sha256
        ).execute()
    except UseCaseException as err:
        raise HTTPException(detail=str(err), status_code=err.status_code)
    except OperationalError:
        raise HTTPException(detail="Error when try create user", status_code=500)


@router.post(
    "/create-admin",
    status_code=status.HTTP_201_CREATED,
    description="This router is to create admin user",
)
async def create_admim():
    try:
        await usecase.CreateUserAdminUseCase(
            user_repository, schema.PostUserSchema
        ).execute()
        return {"message": "Admin user created"}
    except OperationalError:
        raise HTTPException(detail="Error when try create admin", status_code=500)
