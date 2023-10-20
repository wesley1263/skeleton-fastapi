from fastapi import APIRouter, Depends, Request

from app.modules.core.logging import LoggingSkeleton

router = APIRouter()


@router.get(
    "/healthz",
    description="Router to check helth application",
    dependencies=[Depends(LoggingSkeleton())],
)
async def helthcheck(_request: Request):
    return {"msg": "Application running"}
