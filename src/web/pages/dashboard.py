from fastapi import Request
from fastapi import APIRouter

from state.services import templates

from utils.auth import require_login

router = APIRouter()

@router.get("/dashboard")
@require_login
async def dashboard(request: Request):
    return templates.TemplateResponse(name="dashboard.html", request=request)
