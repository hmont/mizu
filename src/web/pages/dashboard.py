from fastapi import APIRouter

from state.services import templates

from utils.auth import require_login
from utils.auth import AuthenticatedRequest

router = APIRouter()

@router.get("/dashboard")
@require_login
async def dashboard(request: AuthenticatedRequest):
    return templates.TemplateResponse(name="dashboard.html", request=request)
