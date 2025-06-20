from uuid import UUID
from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, func

uuidpk = Annotated[UUID, mapped_column(primary_key=True)]
str16 = Annotated[str, mapped_column(String(16))]
str32 = Annotated[str, mapped_column(String(32))]
str64 = Annotated[str, mapped_column(String(64))]
timestamp = Annotated[datetime, mapped_column(server_default=func.now())]
