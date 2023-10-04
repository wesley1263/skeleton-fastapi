from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI

from app.config.settings import get_settings
from app.modules.core.config_enum import ConfigEnum

settings = get_settings()


def init_apm(app: FastAPI):
    """This function is to initialize the Elastic APM."""
    if settings.ENVIRONMENT == ConfigEnum.ENVIRONMENT_PROD.value:
        apm = make_apm_client(
            {
                "SERVICE_NAME": settings.APP_NAME,
                "SERVER_URL": settings.APM_SERVER_URL,
                "ENVIRONMENT": ConfigEnum.ENVIRONMENT_PROD.value,
                "GLOBAL_LABELS": settings.APM_GLOBAL_LABELS,
            }
        )
        app.add_middleware(ElasticAPM, client=apm)
