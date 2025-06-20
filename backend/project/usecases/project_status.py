from uuid import UUID

from repositories.project_status import ProjectStatusRepository
from entities.project_status import GetProjectStatusDTO, CreateUpdateProjectStatusDTO
from mappers.project_status import ProjectStatusMapper


class RetrieveProjectStatusByIdUseCase:
    def __init__(self, repo: ProjectStatusRepository) -> None:
        self.repo = repo

    async def __call__(self, id: UUID) -> GetProjectStatusDTO:
        return await self.repo.selectProjectStatusById(id)


def retrieveProjectStatusByIdUseCase(repo: ProjectStatusRepository) -> RetrieveProjectStatusByIdUseCase:
    return RetrieveProjectStatusByIdUseCase(repo)


class ListProjectStatusUseCase:
    def __init__(self, repo: ProjectStatusRepository) -> None:
        self.repo = repo

    async def __call__(self) -> list[GetProjectStatusDTO]:
        return await self.repo.selectProjectStatuses()


def listProjectStatusUseCase(repo: ProjectStatusRepository) -> ListProjectStatusUseCase:
    return ListProjectStatusUseCase(repo)


class CreateProjectStatusUseCase:
    def __init__(self, repo: ProjectStatusRepository) -> None:
        self.repo = repo

    async def __call__(self, new_project_status: CreateUpdateProjectStatusDTO) -> GetProjectStatusDTO:
        answer_entity = await ProjectStatusMapper.createProjectStatusDTOToEntity(new_project_status)
        return await self.repo.insertProjectStatus(answer_entity)


def createProjectStatusUseCase(repo: ProjectStatusRepository) -> CreateProjectStatusUseCase:
    return CreateProjectStatusUseCase(repo)


class UpdateProjectStatusUseCase:
    def __init__(self, repo: ProjectStatusRepository) -> None:
        self.repo = repo

    async def __call__(self, id: UUID, new_project_status: CreateUpdateProjectStatusDTO) -> GetProjectStatusDTO:
        return await self.repo.updateProjectStatus(id=id, new_project_status=new_project_status)


def updateProjectStatusUseCase(repo: ProjectStatusRepository) -> UpdateProjectStatusUseCase:
    return UpdateProjectStatusUseCase(repo)


class DeleteProjectStatusByIdUseCase:
    def __init__(self, repo: ProjectStatusRepository) -> None:
        self.repo = repo

    async def __call__(self, id: UUID) -> None:
        return await self.repo.deleteProjectStatusById(id)


def deleteProjectStatusByIdUseCase(repo: ProjectStatusRepository) -> DeleteProjectStatusByIdUseCase:
    return DeleteProjectStatusByIdUseCase(repo)
