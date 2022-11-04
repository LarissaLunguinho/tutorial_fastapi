from fastapi import APIRouter
from controllers.papeis_controllers import router as papeis

router = APIRouter()
router.include_router(papeis.router, prefix='/papeis')

