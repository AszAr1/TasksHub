from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ProjectStatusEntity(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str


class GetProjectStatusDTO(BaseModel):
    id: UUID
    name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "ee90c4bc-c6df-4b86-82a2-fa49a3e83c70",
                    "name": "Status 0",
                }
            ]
        }
    }


class CreateUpdateProjectStatusDTO(BaseModel):
    name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Status 0",
                }
            ]
        }
    }
