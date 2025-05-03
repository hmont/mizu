import functools

from typing import Optional
from typing import cast

from fastapi import Request

from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse

from objects.user import User
from objects import user

from state.services import redis

class AuthenticatedRequest(Request):
    def __init__(self, scope, receive, send):
        super().__init__(scope, receive, send)
        self.auth_user: Optional[User] = None

def require_login(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        request = kwargs.get("request")

        if request is None:
            return await func(*args, **kwargs)

        if not isinstance(request, AuthenticatedRequest):
            raise ValueError("Request type must be AuthenticatedRequest")

        request = cast(AuthenticatedRequest, request)

        session_id = get_session_id(request)

        user = await get_user(session_id)

        if not session_id or not user:
            return RedirectResponse("/login")

        request.auth_user = user

        return await func(*args, **kwargs)
    return wrapper

async def get_user(session_id: Optional[str]) -> Optional[User]:
    if session_id is None:
        return None

    user_id = await redis.get(session_id)

    if user_id is None:
        return None

    _user = await user.fetch_one(id=int(user_id))

    return _user

async def end_session(request: Request) -> JSONResponse:
    session_id = get_session_id(request)

    if session_id is None:
        return JSONResponse(content={"message": "Not logged in"})

    await redis.delete(session_id)

    response = JSONResponse(content={"message": "Logged out"})

    response.delete_cookie("session_id")

    return response

def get_session_id(request: Request) -> Optional[str]:
    return request.cookies.get('session_id')