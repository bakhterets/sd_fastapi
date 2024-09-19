"""
CRUD operations:
Create
Read
Update
Delete
"""

from app.core.models import Component, ComponentAttribute

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .schemas import ComponentCreate


async def get_components(session: AsyncSession) -> list[Component]:
    comps = (
        select(Component)
        .options(selectinload(Component.attributes))
        .order_by(Component.id)
    )
    result: Result = await session.execute(comps)
    components = result.scalars().all()
    return list(components)


async def get_component(
    session: AsyncSession, component_id: int
) -> Component | None:
    return await session.get(
        Component, component_id, options=[selectinload(Component.attributes)]
    )


async def create_component(
    session: AsyncSession, component_in: ComponentCreate
) -> Component:
    attributes = [
        ComponentAttribute(name=attr.name, value=attr.value)
        for attr in component_in.attributes
    ]
    component = Component(name=component_in.name, attributes=attributes)
    session.add(component)
    await session.commit()
    await session.refresh(component)
    return component
