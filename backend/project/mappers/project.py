from database.schema import ProjectModel
from entities.project_status import GetProjectStatusDTO
from entities.project import GetProjectDTO, CreateProjectDTO, ProjectEntity, UpdateProjectDTO


class ProjectMapper:
    @classmethod
    async def projectModelToGetDTO(cls, model: ProjectModel, status: GetProjectStatusDTO) -> GetProjectDTO:
        return GetProjectDTO(
            id=model.id,
            name=model.name,
            deadline=model.deadline,
            owner_id=model.owner_id,
            status=status,
        )

    @classmethod
    async def createProjectDTOToEntity(cls, create_project_dto: CreateProjectDTO) -> ProjectEntity:
        return ProjectEntity(
            name=create_project_dto.name,
            deadline=create_project_dto.deadline,
            owner_id=create_project_dto.owner_id,
            status_id=create_project_dto.status_id,
        )

    @classmethod
    async def projectEntityToModel(cls, entity: ProjectEntity) -> ProjectModel:
        return ProjectModel(
            id=entity.id,
            name=entity.name,
            deadline=entity.deadline,
            owner_id=entity.owner_id,
            status_id=entity.status_id
        )
