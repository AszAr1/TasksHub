from uuid import UUID

from repositories.project import ProjectRepository
from entities.project import GetProjectDTO, CreateProjectDTO, UpdateProjectDTO
from mappers.project import ProjectMapper


class RetrieveProjectByIdUseCase:
    def __init__(self, repo: ProjectRepository) -> None:
        self.repo = repo

    async def __call__(self, id: UUID) -> GetProjectDTO:
        return await self.repo.selectProjectById(id)


def retrieveProjectByIdUseCase(repo: ProjectRepository) -> RetrieveProjectByIdUseCase:
    return RetrieveProjectByIdUseCase(repo)


class ListProjectsUseCase:
    def __init__(self, repo: ProjectRepository) -> None:
        self.repo = repo

    async def __call__(self) -> list[GetProjectDTO]:
        return await self.repo.selectProjects()


def listProjectsUseCase(repo: ProjectRepository) -> ListProjectsUseCase:
    return ListProjectsUseCase(repo)


class CreateProjectUseCase:
    def __init__(self, repo: ProjectRepository) -> None:
        self.repo = repo

    async def __call__(self, new_project: CreateProjectDTO) -> GetProjectDTO:
        answer_entity = await ProjectMapper.createProjectDTOToEntity(new_project)
        return await self.repo.insertProject(answer_entity)


def createProjectUseCase(repo: ProjectRepository) -> CreateProjectUseCase:
    return CreateProjectUseCase(repo)


class UpdateProjectUseCase:
    def __init__(self, repo: ProjectRepository) -> None:
        self.repo = repo

    async def __call__(self, id: UUID, new_project: UpdateProjectDTO) -> GetProjectDTO:
        return await self.repo.updateProject(id=id, new_project=new_project)


def updateProjectUseCase(repo: ProjectRepository) -> UpdateProjectUseCase:
    return UpdateProjectUseCase(repo)


class DeleteProjectByIdUseCase:
    def __init__(self, repo: ProjectRepository) -> None:
        self.repo = repo

    async def __call__(self, id: UUID) -> None:
        return await self.repo.deleteProjectById(id)


def deleteProjectByIdUseCase(repo: ProjectRepository) -> DeleteProjectByIdUseCase:
    return DeleteProjectByIdUseCase(repo)
