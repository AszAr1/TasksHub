from database.schema import ProjectStatusModel
from entities.project_status import GetProjectStatusDTO, CreateUpdateProjectStatusDTO, ProjectStatusEntity


class ProjectStatusMapper:
    @classmethod
    async def projectStatusModelToGetDTO(cls, model: ProjectStatusModel) -> GetProjectStatusDTO:
        return GetProjectStatusDTO(
            id=model.id,
            name=model.name,
        )

    @classmethod
    async def createProjectStatusDTOToEntity(
            cls,
            create_project_status_dto: CreateUpdateProjectStatusDTO,
    ) -> ProjectStatusEntity:
        return ProjectStatusEntity(
            name=create_project_status_dto.name,
        )

    @classmethod
    async def projectStatusEntityToModel(cls, entity: ProjectStatusEntity) -> ProjectStatusModel:
        return ProjectStatusModel(
            id=entity.id,
            name=entity.name,
        )
