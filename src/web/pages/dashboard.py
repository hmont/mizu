from fastapi import Request
from fastapi import APIRouter

from fastapi.responses import RedirectResponse 
from fastapi.responses import PlainTextResponse

from state.services import templates

from utils.auth import get_session_id
from utils.auth import get_user
from utils.auth import require_login

router = APIRouter()

@router.get("/dashboard")
@require_login
async def dashboard(request: Request):
    return templates.TemplateResponse(name="dashboard.html", request=request)