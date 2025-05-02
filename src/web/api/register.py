import bcrypt

from fastapi import APIRouter
from fastapi import Request

from fastapi.responses import JSONResponse

from state.services import templates

from web import web_router

from objects import user

router = APIRouter()

@router.post("/register")
async def register(request: Request):
    data = await request.json()

    username = str(data['username'])
    password = str(data['password']).encode()

    pw_hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode()

    if await user.fetch_one(username=username) is not None:
        return JSONResponse(status_code=200,
                            content={"message": "User with that username already exists"})

    await user.create(
        username=username,
        password_hash=pw_hashed
    )

    return JSONResponse(status_code=200, content={"message": "Account created - you may now login"})

@web_router.get("/register")
async def get_register(request: Request):
    return templates.TemplateResponse(name="register.html", request=request)