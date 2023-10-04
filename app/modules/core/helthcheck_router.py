from fastapi import APIRouter, Depends, Request

from app.modules.core.logging import LoggingUnder

router = APIRouter()


@router.get(
    "/health-check",
    description="Router to check helth application",
    dependencies=[Depends(LoggingUnder())],
)
async def helthcheck(_request: Request):
    return {"msg": "Application running"}
