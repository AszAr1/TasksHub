from fastapi import status, Request, Response
from fastapi.responses import JSONResponse

from exceptions import (
    EmptyListResponseException,
    BadRequestException,
    NotFoundException,
)


def emptyListResponseExceptionHandler(request: Request, exc: EmptyListResponseException) -> Response:
    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
        headers={"X-Error": f"{exc.__class__.__name__}"},
    )


def badRequestExceptionHandler(request: Request, exc: BadRequestException) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'message': f"{exc.message}"},
        headers={"X-Error": f"{exc.__class__.__name__}"},
    )


def notFoundExceptionHandler(request: Request, exc: NotFoundException) -> Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'message': f"{exc.message}"},
        headers={"X-Error": f"{exc.__class__.__name__}"},
    )
