"""
CRUD operations:
"""

from app.core.models import (
    Component,
    ComponentAttribute,
    Incident,
    IncidentStatus,
)

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .schemas import ComponentCreate
from .schemas import IncidentCreate


async def get_components(session: AsyncSession) -> list[Component]:
    query = (
        select(Component)
        .options(
            selectinload(Component.attributes),
            selectinload(Component.incidents).selectinload(Incident.updates),
        )
        .order_by(Component.id)
    )
    result: Result = await session.execute(query)
    components = result.scalars().all()
    return list(components)


async def get_component(
    session: AsyncSession, component_id: int
) -> Component | None:
    query = (
        select(Component)
        .where(Component.id == component_id)
        .options(
            selectinload(Component.attributes),
            selectinload(Component.incidents),
        )
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()


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


async def get_component_by_name_and_attributes(
    session: AsyncSession, name: str, attributes: list[dict[str, str]]
) -> list[Component]:
    query = (
        select(Component)
        .filter(Component.name == name)
        .join(Component.attributes)
        .filter(
            ComponentAttribute.name.in_([attr["name"] for attr in attributes]),
            ComponentAttribute.value.in_(
                [attr["value"] for attr in attributes]
            ),
        )
    )

    result = await session.execute(query)
    return list(result.scalars().all())


async def get_incidents(session: AsyncSession) -> list[Incident]:
    query = (
        select(Incident)
        .options(
            selectinload(Incident.updates),
            selectinload(Incident.components),
        )
        .order_by(Incident.id)
    )
    result: Result = await session.execute(query)
    incidents = result.scalars().all()
    return list(incidents)


async def get_incident(
    session: AsyncSession, incident_id: int
) -> Incident | None:
    query = (
        select(Incident)
        .where(Incident.id == incident_id)
        .options(
            selectinload(Incident.updates),
            selectinload(Incident.components),
        )
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def create_incident(
    session: AsyncSession, incident_in: IncidentCreate
) -> Incident | None:
    updates = [
        IncidentStatus(status=upd.status, text=upd.text)
        for upd in incident_in.updates
    ]
    components = []

    for comp_data in incident_in.components:
        comp_instance = await get_component_by_name_and_attributes(
            session=session,
            name=comp_data.name,
            attributes=[
                {"name": attr.name, "value": attr.value}
                for attr in comp_data.attributes
            ],
        )

        if not comp_instance:
            return None

        components.extend(comp_instance)

    incident = Incident(
        text=incident_in.text,
        impact=incident_in.impact,
        start_date=incident_in.start_date,
        end_date=incident_in.end_date,
        components=components,
        updates=updates,
    )

    session.add(incident)
    await session.commit()
    await session.refresh(incident)

    return incident
