from typing import List

from fastapi import APIRouter, HTTPException, status,Depends

from schemas.user import User
from services.user import UserService

from auth import validate_iap_jwt
from schemas.auth import IAPJwtPayload

router = APIRouter()

user_services = UserService()

@router.get('/users', response_model=List[User])
async def list_users(jwt_token: IAPJwtPayload = Depends(validate_iap_jwt)):
    # Googleのプロファイル取得の設定してないので一旦メールの前段を名前にする
    username, _ = user_services.split_email(jwt_token.email)
    user_services.check_has_user_or_create(username, jwt_token.email)
    users = user_services.get_all_user()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return users

@router.get("/users/docs")
def list_user_doc(jwt_token: IAPJwtPayload = Depends(validate_iap_jwt)):
    # Googleのプロファイル取得の設定してないので一旦メールの前段を名前にする
    username, _ = user_services.split_email(jwt_token.email)
    user_services.check_has_user_or_create(username, jwt_token.email)
    users_docs = user_services.get_all_doc()
    if not users_docs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return users_docs
