from typing import List

from fastapi import APIRouter, status, Request

from schemas.user import User
from services.user import UserService


router = APIRouter()

@router.get("/jwt")
def get_jwt(req: Request):
    return {"headers": req.headers}
