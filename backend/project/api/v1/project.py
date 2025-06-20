from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.exc import IntegrityError

from exceptions import EmptyListResponseException, BadRequestException
from entities.project import GetProjectDTO, CreateProjectDTO, UpdateProjectDTO
from usecases.project import (
    ListProjectsUseCase,
    listProjectsUseCase,

    CreateProjectUseCase,
    createProjectUseCase,

    RetrieveProjectByIdUseCase,
    retrieveProjectByIdUseCase,

    UpdateProjectUseCase,
    updateProjectUseCase,

    DeleteProjectByIdUseCase,
    deleteProjectByIdUseCase,
)
from repositories.project import ProjectRepository

project_router = APIRouter(
    prefix="/projects", tags=["Projects"]
)


@project_router.get('', status_code=status.HTTP_200_OK, response_model=list[GetProjectDTO])
async def getProjects(
        use_case: ListProjectsUseCase = Depends(lambda: listProjectsUseCase(ProjectRepository()))
) -> list[GetProjectDTO]:
    projects = await use_case()
    if len(projects) == 0:
        raise EmptyListResponseException("No projects")

    return projects


@project_router.get('/{project_id}', status_code=status.HTTP_200_OK, response_model=GetProjectDTO)
async def getProjectById(
        project_id: UUID,
        use_case: RetrieveProjectByIdUseCase = Depends(lambda: retrieveProjectByIdUseCase(ProjectRepository()))
):
    return await use_case(project_id)


@project_router.post('/create', status_code=status.HTTP_201_CREATED, response_model=GetProjectDTO)
async def createProject(
        create_project_dto: CreateProjectDTO,
        use_case: CreateProjectUseCase = Depends(lambda: createProjectUseCase(ProjectRepository()))
) -> GetProjectDTO:
    try:
        return await use_case(create_project_dto)
    except IntegrityError as e:
        raise BadRequestException(str(e.args[0]))


@project_router.patch('/{project_id}', status_code=status.HTTP_200_OK, response_model=GetProjectDTO)
async def updateProject(
        project_id: UUID,
        update_project_dto: UpdateProjectDTO,
        use_case: UpdateProjectUseCase = Depends(lambda: updateProjectUseCase(ProjectRepository()))
) -> GetProjectDTO:
    try:
        return await use_case(project_id, update_project_dto)
    except IntegrityError as e:
        raise BadRequestException(e.args)


@project_router.delete('/{project_id}', status_code=status.HTTP_200_OK)
async def deleteProjectById(
        project_id: UUID,
        use_case: DeleteProjectByIdUseCase = Depends(lambda: deleteProjectByIdUseCase(ProjectRepository()))
) -> None:
    await use_case(project_id)
