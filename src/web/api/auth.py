import bcrypt

import uuid

from fastapi import APIRouter
from fastapi import Request
from fastapi import Response

from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse

from datetime import timedelta
from datetime import datetime
from datetime import timezone

from web import web_router

from objects import user

from state.services import redis
from state.services import templates

from utils.auth import get_user

router = APIRouter()

@web_router.get("/test")
async def test(request: Request):
    user = await get_user(request)
    
    if user is None:
        return PlainTextResponse("Not logged in")
    
    return PlainTextResponse(f"Logged in as {user['username']}")
    
@web_router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(name="login.html", request=request)

@router.post("/auth")
async def auth(request: Request, response: Response):
    session_user = await get_user(request)
    
    if session_user is not None:
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