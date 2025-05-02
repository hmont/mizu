import uuid

from datetime import timedelta
from datetime import datetime
from datetime import timezone

import bcrypt

from fastapi import APIRouter
from fastapi import Request
from fastapi import Response

from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse
from fastapi.responses import RedirectResponse

from web import web_router

from objects import user

from state.services import redis
from state.services import templates

from utils.auth import get_user
from utils.auth import get_session_id
from utils.auth import end_session

router = APIRouter()

@web_router.get("/login")
async def login(request: Request):
    session_id = get_session_id(request)

    if not session_id or not await get_user(session_id):
        return templates.TemplateResponse(name="login.html", request=request)

    return RedirectResponse(url="/dashboard")

@router.post("/logout")
async def logout(request: Request):
    return await end_session(request)

@router.post("/auth")
async def auth(request: Request, response: Response):
    session_id = get_session_id(request)

    if session_id is not None:
        return JSONResponse(status_code=200,
                                content={"message": "Already authenticated"})

    data = await request.json()

    username = str(data['username'])
    password = str(data['password']).encode()

    _user = await user.fetch_one(username=username)

    _session_id = request.cookies.get('session_id')

    if _session_id is not None:
        if await redis.get(_session_id):
            return JSONResponse(status_code=200,
                                content={"message": "Already authenticated"})

        request.cookies.pop(_session_id)

    if _user is None:
        return JSONResponse(status_code=401,
                            content={"message": "Invalid username/password combination"})

    if not bcrypt.checkpw(password, _user['password_hash'].encode()):
        return JSONResponse(status_code=401,
                            content={"message": "Invalid username/password combination"})

    session_id = str(uuid.uuid4())

    expiry = timedelta(days=7)

    await redis.set(session_id, _user['id'], ex=expiry)

    response = JSONResponse(status_code=200, content={"message": "Authenticated"})

    response.set_cookie(key="session_id",
                        value=session_id,
                        httponly=True,
                        secure=True,
                        samesite="lax",
                        expires=datetime.now(timezone.utc) + expiry)

    return response