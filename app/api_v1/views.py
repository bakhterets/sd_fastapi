from app.core.models.db_manager import db_manager

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import ComponentCreate
from .schemas import ComponentRead
from .schemas import IncidentRead
from .schemas import IncidentCreate


router = APIRouter()


@router.get("/component_status", response_model=list[ComponentRead])
async def get_components(
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    return await crud.get_components(session=session)


@router.get("/component_status/{component_id}")
async def get_component(
    component_id: int,
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    component = await crud.get_component(
        session=session, component_id=component_id
    )
    if component is not None:
        return component

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Component with id: {component_id} not found",
    )


@router.post("/component_status", response_model=ComponentRead)
async def create_component(
    component_in: ComponentCreate,
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    return await crud.create_component(
        session=session, component_in=component_in
    )


@router.get("/incidents", response_model=list[IncidentRead])
async def get_incidents(
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    return await crud.get_incidents(session=session)


@router.get("/incidents/{incident_id}", response_model=IncidentRead)
async def get_incident(
    incident_id: int,
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    incident = await crud.get_incident(
        session=session,
        incident_id=incident_id,
    )
    if incident is not None:
        return incident

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Incident with id: {incident_id} not found",
    )


@router.post("/incidents", response_model=IncidentRead)
async def create_incident(
    incident_in: IncidentCreate,
    session: AsyncSession = Depends(db_manager.session_dependency),
):

    incident = await crud.create_incident(
        session=session, incident_in=incident_in
    )

    if not incident:
        raise HTTPException(
            status_code=404, detail="One or more components were not found."
        )

    return incident
