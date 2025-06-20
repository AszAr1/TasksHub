from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from entities.project_status import GetProjectStatusDTO


class ProjectEntity(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    deadline: datetime
    owner_id: UUID
    status_id: UUID


class GetProjectDTO(BaseModel):
    id: UUID
    name: str
    deadline: datetime
    owner_id: UUID
    status: GetProjectStatusDTO

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "ee90c4bc-c6df-4b86-82a2-fa49a3e83c70",
                    "name": "Project 0",
                    "deadline": "2025-01-01T0:00:00",
                    "owner_id": "ee90c4bc-c6df-4b86-82a2-fa49a3e83c70",
                    "status": "Status entity",
                }
            ]
        }
    }


class CreateProjectDTO(BaseModel):
    name: str
    deadline: datetime
    owner_id: UUID
    status_id: UUID

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Project 0",
                    "deadline": "2025-01-01T0:00:00",
                    "owner_id": "ee90c4bc-c6df-4b86-82a2-fa49a3e83c70",
                    "status_id": "ee90c4bc-c6df-4b86-82a2-fa49a3e83c70",
                }
            ]
        }
    }


class UpdateProjectDTO(BaseModel):
    name: str | None = None
    deadline: datetime | None = None
    status_id: UUID | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Project 0",
                    "deadline": "2025-01-01T0:00:00",
                    "status_id": "ee90c4bc-c6df-4b86-82a2-fa49a3e83c70",
                }
            ]
        }
    }
