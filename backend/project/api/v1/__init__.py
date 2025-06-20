from fastapi import APIRouter
from .project import project_router
from .project_status import project_status_router

v1_router = APIRouter(
    prefix='/v1'
)

v1_router.include_router(project_router)
v1_router.include_router(project_status_router)


