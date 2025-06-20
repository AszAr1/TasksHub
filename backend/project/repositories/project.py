from uuid import UUID

from sqlalchemy import select

from database import async_session_factory
from database.schema import ProjectModel, ProjectStatusModel
from entities.project import ProjectEntity, GetProjectDTO, UpdateProjectDTO
from exceptions import NotFoundException
from mappers.project_status import ProjectStatusMapper
from mappers.project import ProjectMapper


class ProjectRepository:
    async def insertProject(self, new_project: ProjectEntity) -> GetProjectDTO:
        async with async_session_factory() as session:
            project_model = await ProjectMapper.projectEntityToModel(new_project)
            session.add(project_model)

            await session.flush()

            project_status_model = await session.get(ProjectStatusModel, project_model.status_id)
            if not project_status_model:
                raise NotFoundException(f"No project status with id: {project_model.status_id}")

            get_project_dto = await ProjectMapper.projectModelToGetDTO(
                model=project_model,
                status=await ProjectStatusMapper.projectStatusModelToGetDTO(project_status_model),
            )

            await session.commit()

        return get_project_dto

    async def selectProjects(self) -> list[GetProjectDTO]:
        async with async_session_factory() as session:
            project_models = (await session.execute(
                select(ProjectModel)
            )).scalars().all()

            get_project_dtos = []
            for project_model in project_models:
                project_status_model = await session.get(ProjectStatusModel, project_model.status_id)

                get_project_dtos.append(await ProjectMapper.projectModelToGetDTO(
                    project_model,
                    await ProjectStatusMapper.projectStatusModelToGetDTO(project_status_model)
                ))

        return get_project_dtos

    async def selectProjectById(self, id: UUID) -> GetProjectDTO:
        async with async_session_factory() as session:
            project_model = await session.get(ProjectModel, id)
            print(f'selectProjectById: {project_model=}')
            if not project_model:
                raise NotFoundException(f"No project with id: {id}")

            project_status_model = await session.get(ProjectStatusModel, project_model.status_id)

            get_project_dto = await ProjectMapper.projectModelToGetDTO(
                project_model,
                await ProjectStatusMapper.projectStatusModelToGetDTO(project_status_model)
            )

        return get_project_dto

    async def updateProject(self, id: UUID, new_project: UpdateProjectDTO) -> GetProjectDTO:
        async with async_session_factory() as session:
            project_model = await session.get(ProjectModel, id)
            if not project_model:
                raise NotFoundException(f"No project with id: {id}")

            project_model.name = new_project.name if new_project.name else project_model.name
            project_model.deadline = new_project.deadline if new_project.deadline else project_model.deadline
            project_model.status_id = new_project.status_id if new_project.status_id else project_model.status_id

            await session.flush()

            project_status_model = await session.get(ProjectStatusModel, project_model.status_id)

            get_project_dto = await ProjectMapper.projectModelToGetDTO(
                project_model,
                await ProjectStatusMapper.projectStatusModelToGetDTO(project_status_model),
            )

            await session.commit()

        return get_project_dto

    async def deleteProjectById(self, id: UUID) -> None:
        async with async_session_factory() as session:
            project_model = await session.get(ProjectModel, id)
            if not project_model:
                raise NotFoundException(f"No project with id: {id}")

            await session.delete(project_model)

            await session.commit()
