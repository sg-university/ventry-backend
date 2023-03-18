from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from sqlmodel.ext.asyncio.session import AsyncSession

from app.outers.settings.datastore_settings import datastore_setting

engine = create_async_engine(
    url=datastore_setting.URL,
    poolclass=NullPool,
)


async def create_session() -> AsyncSession:
    async with AsyncSession(engine) as session:
        return session
