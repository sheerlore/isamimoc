import os

from google.auth.transport import requests
from google.oauth2 import id_token

from fastapi import Request
from jose import jwt


def validate_iap_jwt(iap_jwt, expected_audience):
    """Validate an IAP JWT.

    Args:
      iap_jwt: The contents of the X-Goog-IAP-JWT-Assertion header.
      expected_audience: The Signed Header JWT audience. See
          https://cloud.google.com/iap/docs/signed-headers-howto
          for details on how to get this value.

    Returns:
      (user_id, user_email, error_str).
    """

    try:
        decoded_jwt = id_token.verify_token(
            iap_jwt,
            requests.Request(),
            audience=expected_audience,
            certs_url="https://www.gstatic.com/iap/verify/public_key",
        )
        # return (decoded_jwt["sub"], decoded_jwt["email"], "")
        return decoded_jwt
    except Exception as e:
        return (None, None, f"**ERROR: JWT validation error {e}**")


def validate_jwt(request: Request):
    jwt_token = request.headers.get("x-goog-iap-jwt-assertion")
    expected_audience = os.getenv("EXPECTED_AUD")

    # try:
    
    # except Exception as e:
    #     return 