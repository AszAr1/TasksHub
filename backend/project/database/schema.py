from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from .types import uuidpk, str16, str32


class Base(DeclarativeBase):
    def __repr__(self):
        attrs = [f'{col}: {getattr(self, col)}' for col in self.__table__.columns.keys()]
        return f"{self.__class__.__name__}:({', '.join(attrs)})"


class ProjectStatusModel(Base):
    __tablename__ = 'project_statuses'

    id: Mapped[uuidpk]
    name: Mapped[str16]

    projects: Mapped[list["ProjectModel"]] = relationship(
        back_populates='status'
    )


class ProjectModel(Base):
    __tablename__ = 'projects'

    id: Mapped[uuidpk]
    name: Mapped[str32]
    deadline: Mapped[datetime]
    owner_id: Mapped[UUID]
    status_id: Mapped[UUID] = mapped_column(ForeignKey('project_statuses.id', ondelete='CASCADE'))

    status: Mapped[ProjectStatusModel] = relationship(
        back_populates='projects',
    )