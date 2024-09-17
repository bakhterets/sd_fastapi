from fastapi import APIRouter

from .components.views import router as components_router

router = APIRouter()
router.include_router(router=components_router, prefix="/components")
