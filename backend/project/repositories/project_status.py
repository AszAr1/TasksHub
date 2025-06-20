from uuid import UUID

from sqlalchemy import select

from database import async_session_factory
from entities.project_status import ProjectStatusEntity, GetProjectStatusDTO, CreateUpdateProjectStatusDTO
from database.schema import ProjectStatusModel
from exceptions import NotFoundException
from mappers.project_status import ProjectStatusMapper


class ProjectStatusRepository:
    async def insertProjectStatus(self, new_project_status: ProjectStatusEntity) -> GetProjectStatusDTO:
        async with async_session_factory() as session:
            project_status_model = await ProjectStatusMapper.projectStatusEntityToModel(new_project_status)
            session.add(project_status_model)

            get_project_status_dto = await ProjectStatusMapper.projectStatusModelToGetDTO(project_status_model)

            await session.commit()

        return get_project_status_dto

    async def selectProjectStatuses(self) -> list[GetProjectStatusDTO]:
        async with async_session_factory() as session:
            project_status_models = (await session.execute(
                select(ProjectStatusModel)
            )).scalars().all()

            get_project_status_dtos = [
                await ProjectStatusMapper.projectStatusModelToGetDTO(project_status_model)
                for project_status_model in project_status_models
            ]

        return get_project_status_dtos

    async def selectProjectStatusById(self, id: UUID) -> GetProjectStatusDTO:
        async with async_session_factory() as session:
            project_status_model = await session.get(ProjectStatusModel, id)
            if not project_status_model:
                raise NotFoundException(f"No project status with id: {id}")

            get_project_status_dto = await ProjectStatusMapper.projectStatusModelToGetDTO(project_status_model)

        return get_project_status_dto

    async def updateProjectStatus(
            self,
            id: UUID,
            new_project_status: CreateUpdateProjectStatusDTO
    ) -> GetProjectStatusDTO:
        async with (async_session_factory() as session):
            project_status_model = await session.get(ProjectStatusModel, id)
            if not project_status_model:
                raise NotFoundException(f"No project status with id: {id}")

            project_status_model.name = new_project_status.name if new_project_status.name \
                else project_status_model.name

            await session.flush()

            get_project_status_dto = await ProjectStatusMapper.projectStatusModelToGetDTO(project_status_model)

            await session.commit()

        return get_project_status_dto

    async def deleteProjectStatusById(self, id: UUID) -> None:
        async with async_session_factory() as session:
            project_status_model = await session.get(ProjectStatusModel, id)
            if not project_status_model:
                raise NotFoundException(f"No project status with id: {id}")

            await session.delete(project_status_model)

            await session.commit()
