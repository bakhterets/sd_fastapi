from app.core.models.db_manager import db_manager

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Component
from .schemas import ComponentCreate

router = APIRouter(tags=["Components"])


@router.get("/", response_model=list[Component])
async def get_components(
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    return await crud.get_components(session=session)


@router.get("/{component_id}")
async def get_comppnent(
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


@router.post("/", response_model=Component)
async def create_component(
    component_in: ComponentCreate,
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    return await crud.create_component(
        session=session, component_in=component_in
    )
