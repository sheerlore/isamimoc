from typing_extensions import Annotated

from fastapi import APIRouter, status, Request, Header, HTTPException, Depends
from jose import jwt
from auth import validate_iap_jwt
from schemas.auth import IAPJwtPayload

from config import get_settings, Settings

router = APIRouter()

@router.get("/jwt")
def get_jwt(jwt_token: IAPJwtPayload = Depends(validate_iap_jwt)):
    return {"token": jwt_token}