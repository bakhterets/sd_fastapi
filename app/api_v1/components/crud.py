"""
CRUD operations:
Create
Read
Update
Delete
"""

from app.core.models import Component

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ComponentCreate


async def get_components(session: AsyncSession) -> list[Component]:
    comps = select(Component).order_by(Component.id)
    result: Result = await session.execute(comps)
    components = result.scalars().all()
    return list(components)


async def get_component(
    session: AsyncSession, component_id: int
) -> Component | None:
    return await session.get(Component, component_id)


async def create_component(
    session: AsyncSession, component_in: ComponentCreate
) -> Component:
    component = Component(**component_in.model_dump())
    session.add(component)
    await session.commit()
    await session.refresh(component)
    return component
