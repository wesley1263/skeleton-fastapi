from enum import Enum


class ConfigEnum(str, Enum):
    ENVIRONMENT_DEV = "dev"
    ENVIRONMENT_PROD = "producao"
    ENVIRONMENT_HOMOLOG = "homolog"
