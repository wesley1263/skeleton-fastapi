from fastapi import APIRouter, Depends, status, HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page, paginate

from app.abstracts.usecase_exception import UseCaseException
from app.config.settings import get_settings
from app.modules.core.auth_bearer import JWTBearer
from app.modules.core.logging import LoggingSkeleton
from app.modules.user import schema, usecase
from app.modules.user.repository import UserRepository

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
    users = await usecase.GetUsersUseCase(user_repository).execute()
    return paginate(users)


@router.get(
    "/{id}",
    description="Router to one user by id",
    response_model=schema.GetUserSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_user(id: int):
    return await usecase.GetUserUseCase(id, user_repository).execute()


@router.post(
    "/",
    description="This router is to create new user",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.GetUserSchema,
    dependencies=[Depends(JWTBearer())],
)
async def post_user(payload: schema.PostUserSchema):
    try:
        _schema = schema.GetUserSchema
        return await usecase.CreateUserUseCase(payload, user_repository, _schema).execute()
    except UseCaseException as err:
        raise HTTPException(detail=str(err), status_code=err.status_code)


@router.get(
    "/email/{email}",
    description="This router is to get one user by email",
    status_code=status.HTTP_200_OK,
    response_model=schema.GetUserSchema,
    dependencies=[Depends(JWTBearer())],
)
async def get_user_by_email(email: str):
    return await usecase.GetUserByEmailUseCase(email, user_repository).execute()


@router.put(
    "/{id}",
    description="This router is to update user",
    status_code=status.HTTP_200_OK,
    response_model=schema.GetUserSchema,
    dependencies=[Depends(JWTBearer()), Depends(JWTBearer())],
)
async def put_user(id: int, payload: schema.UpdateUserSchema):
    return await usecase.UpdateUserUseCase(payload, id, user_repository).execute()


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=schema.JWTUserSchema,
    description="This router is to login user",
)
async def login(payload: schema.LoginUserSchema, authorize: AuthJWT = Depends()):
    return await usecase.LoginUseCase(payload, authorize, user_repository).execute()


@router.post(
    "/create-admin",
    status_code=status.HTTP_201_CREATED,
    description="This router is to create admin user",
)
async def create_admim():
    await usecase.CreateUserAdminUseCase(user_repository).execute()
    return {"message": "Admin user created"}
