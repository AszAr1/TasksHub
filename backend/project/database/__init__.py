from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from db_config import settings

async_engine = create_async_engine(
    url=settings.databaseUrlAsyncPG,
)

async_session_factory = async_sessionmaker(bind=async_engine)
