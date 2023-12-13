from fastapi import APIRouter

from api.routes.model_predict import model_router

router = APIRouter()
router.include_router(model_router, prefix="/predict", tags=["Model"])

__all__ = ["router"]
