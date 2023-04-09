from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from sqlmodel.ext.asyncio.session import AsyncSession

from app.outers.settings.datastore_settings import datastore_setting


class DataStoreUtility:
    def __init__(self):
        self.engine = create_async_engine(
            url=datastore_setting.URL,
            poolclass=NullPool,
        )

    async def create_session(self) -> AsyncSession:
        async with AsyncSession(self.engine) as session:
            return session
