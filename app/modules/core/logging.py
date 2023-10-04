import logging
import sys
from datetime import datetime
from uuid import uuid4

from fastapi import Request


class LoggingUnder:
    def __init__(self):
        self.logger = logging
        self.logger.basicConfig(
            format="%(message)s", stream=sys.stdout, level=logging.INFO
        )

    async def __call__(self, request: Request):
        self.logger.info(
            {
                "level": "DEBUG",
                "uuid": uuid4().hex,
                "time": datetime.now().strftime("%Y-%m-%d at %H:%M:%S.%f")[:-3],
                "url": f"{request.url.scheme}://{request.url.hostname}",
                "path": request.url.path,
            }
        )
