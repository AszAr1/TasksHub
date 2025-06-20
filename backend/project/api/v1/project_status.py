from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.exc import IntegrityError

from exceptions import EmptyListResponseException, BadRequestException
from entities.project_status import GetProjectStatusDTO, CreateUpdateProjectStatusDTO
from usecases.project_status import (
    ListProjectStatusUseCase,
    listProjectStatusUseCase,

    CreateProjectStatusUseCase,
    createProjectStatusUseCase,

    RetrieveProjectStatusByIdUseCase,
    retrieveProjectStatusByIdUseCase,

    UpdateProjectStatusUseCase,
    updateProjectStatusUseCase,

    DeleteProjectStatusByIdUseCase,
    deleteProjectStatusByIdUseCase,
)
from repositories.project_status import ProjectStatusRepository

project_status_router = APIRouter(
    prefix="/project_statuses", tags=["Project Statuses"]
)


@project_status_router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=list[GetProjectStatusDTO]
)
async def getProjects(
        use_case: ListProjectStatusUseCase = Depends(
            lambda: listProjectStatusUseCase(ProjectStatusRepository())
        )
) -> list[GetProjectStatusDTO]:
    project_statuses = await use_case()
    if len(project_statuses) == 0:
        raise EmptyListResponseException("No project statuses")

    return project_statuses


@project_status_router.get(
    '/{project_status_id}',
    status_code=status.HTTP_200_OK,
    response_model=GetProjectStatusDTO
)
async def getProjectById(
        project_status_id: UUID,
        use_case: RetrieveProjectStatusByIdUseCase = Depends(
            lambda: retrieveProjectStatusByIdUseCase(ProjectStatusRepository())
        )
):
    return await use_case(project_status_id)


@project_status_router.post(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=GetProjectStatusDTO
)
async def createProject(
        create_project_status_dto: CreateUpdateProjectStatusDTO,
        use_case: CreateProjectStatusUseCase = Depends(
            lambda: createProjectStatusUseCase(ProjectStatusRepository())
        )
) -> GetProjectStatusDTO:
    try:
        return await use_case(create_project_status_dto)
    except IntegrityError as e:
        raise BadRequestException(str(e.args[0]))


@project_status_router.patch(
    '/{project_status_id}',
    status_code=status.HTTP_200_OK,
    response_model=GetProjectStatusDTO
)
async def updateProject(
        project_status_id: UUID,
        update_project_status_dto: CreateUpdateProjectStatusDTO,
        use_case: UpdateProjectStatusUseCase = Depends(
            lambda: updateProjectStatusUseCase(ProjectStatusRepository())
        )
) -> GetProjectStatusDTO:
    try:
        return await use_case(project_status_id, update_project_status_dto)
    except IntegrityError as e:
        raise BadRequestException(e.args)


@project_status_router.delete(
    '/{project_status_id}',
    status_code=status.HTTP_200_OK
)
async def deleteProjectById(
        project_status_id: UUID,
        use_case: DeleteProjectStatusByIdUseCase = Depends(
            lambda: deleteProjectStatusByIdUseCase(ProjectStatusRepository())
        )
) -> None:
    await use_case(project_status_id)
