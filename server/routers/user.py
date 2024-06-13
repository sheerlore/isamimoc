from typing import List

from fastapi import APIRouter, HTTPException, status

from schemas.user import User
from services.user import UserService

router = APIRouter()

user_services = UserService()

@router.get(
    '/users',
    response_model=List[User],
    tags=["user"]
)
def list_users():
    users = user_services.get_all_user()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return users