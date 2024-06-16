from typing import List

from fastapi import APIRouter, HTTPException, status,Depends

from schemas.user import UserFull, TmpStatus, IsAFK, SeatPos
from services.user import UserService

from auth import validate_iap_jwt
from schemas.auth import IAPJwtPayload

router = APIRouter()

user_services = UserService()

@router.get('/users', response_model=List[UserFull])
async def list_users(jwt_token: IAPJwtPayload = Depends(validate_iap_jwt)):
    # Googleのプロファイル取得の設定してないので一旦メールの前段を名前にする
    username, _ = user_services.split_email(jwt_token.email)
    user_services.check_has_user_or_create(username, jwt_token.email)
    users = user_services.get_all_user()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return users

@router.post('/users/is-afk')
async def update_tmp_status(data: IsAFK, jwt_token: IAPJwtPayload = Depends(validate_iap_jwt)):
    username, _ = user_services.split_email(jwt_token.email)
    user_services.check_has_user_or_create(username, jwt_token.email)
    user_services.update_self_is_afk(jwt_token.email, data)

    return {"ok": data}

@router.post('/users/tmp-status')
async def update_tmp_status(data: TmpStatus, jwt_token: IAPJwtPayload = Depends(validate_iap_jwt)):
    username, _ = user_services.split_email(jwt_token.email)
    user_services.check_has_user_or_create(username, jwt_token.email)
    user_services.update_self_tmp_status(jwt_token.email, data)

    return {"ok": data}
    
@router.post('/users/seat-pos')
async def update_tmp_status(data: SeatPos, jwt_token: IAPJwtPayload = Depends(validate_iap_jwt)):
    username, _ = user_services.split_email(jwt_token.email)
    user_services.check_has_user_or_create(username, jwt_token.email)
    user_services.update_self_seat_pos(jwt_token.email, data)

    return {"ok": data}