from fastapi import FastAPI

from api.exception_handlers import (
    emptyListResponseExceptionHandler,
    badRequestExceptionHandler,
    notFoundExceptionHandler,
)
from api.v1 import v1_router
from exceptions import (
    EmptyListResponseException,
    BadRequestException,
    NotFoundException,
)

app = FastAPI()

app.add_exception_handler(
    exc_class_or_status_code=EmptyListResponseException,
    handler=emptyListResponseExceptionHandler,
)
app.add_exception_handler(
    exc_class_or_status_code=BadRequestException,
    handler=badRequestExceptionHandler,
)
app.add_exception_handler(
    exc_class_or_status_code=NotFoundException,
    handler=notFoundExceptionHandler,
)

app.include_router(v1_router)
