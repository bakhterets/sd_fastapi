from asyncio import current_task
from typing import AsyncGenerator

from app.core.config import settings

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///example.sqlite"


class DatabaseManager:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(
        self,
    ) -> AsyncGenerator[AsyncSession, None]:
        session = self.get_scoped_session()
        yield session
        await session.close()


db_manager = DatabaseManager(
    url=settings.db.url,
    echo=settings.db.echo,
)
