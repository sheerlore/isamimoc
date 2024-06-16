from typing_extensions import Annotated

from fastapi import APIRouter, status, Request, Header, HTTPException, Depends
from jose import jwt
from internal.auth import validate_iap_jwt

from config import get_settings, Settings

router = APIRouter()

@router.get("/jwt")
def get_jwt(req: Request):
    return {"headers": req.headers}

@router.get("/jwt/spec")
def get_jwt(
    settings: Annotated[Settings, Depends(get_settings)],
    x_goog_iap_jwt_assertion: str = Header()
):
    expected_aud = settings.expected_aud
    if not expected_aud:
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    jwt_payload = validate_iap_jwt(x_goog_iap_jwt_assertion, expected_aud)

    return {"jwt": jwt_payload}