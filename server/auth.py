from typing_extensions import Annotated
from google.auth.transport import requests
from google.oauth2 import id_token
from fastapi import Request, HTTPException, status, Depends
from fastapi.security import APIKeyHeader
from schemas.auth import IAPJwtPayload
from config import get_settings, Settings

iap_jwt_token_header= APIKeyHeader(name="x-goog-iap-jwt-assertion", auto_error=True)

# JWTが正しいかどうか検証
def validate_iap_jwt(
    settings: Annotated[Settings, Depends(get_settings)],
    jwt_token: str = Depends(iap_jwt_token_header),
):
    expected_aud = settings.expected_aud
    expected_iss = settings.expected_iss

    if not expected_aud or not expected_iss:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="読み込みエラー")

    try:
        decoded_jwt = id_token.verify_token(
            jwt_token,
            requests.Request(),
            audience=expected_aud,
            certs_url="https://www.gstatic.com/iap/verify/public_key",
        )
        if decoded_jwt['iss'] != expected_iss:
            raise Exception("iss different error")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"JWTトークンの解析に失敗: {e}")

    return IAPJwtPayload(
        sub = decoded_jwt['sub'],
        email = decoded_jwt['email']
    )
