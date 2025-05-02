from typing import Optional

from fastapi import Request

from objects.user import User
from objects import user

from state.services import redis

async def get_user(request: Request) -> Optional[User]:
    _session_id = request.cookies.get('session_id')
    
    if _session_id is None:
        return None
    
    user_id = await redis.get(_session_id)
    
    if user_id is None:
        return None
    
    _user = await user.fetch_one(id=int(user_id))
        
    return _user