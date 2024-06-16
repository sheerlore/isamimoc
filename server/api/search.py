from typing import List

from fastapi import APIRouter, Depends

from schemas.auth import IAPJwtPayload
from auth import validate_iap_jwt

from services.search import SearchService
from schemas.user import UserFull

router = APIRouter()

search_services = SearchService()

# ユーザー検索
@router.get("/search/user", response_model=List[UserFull])
def search_users( q: str | None = None, limit: int = 5, jwt_token: IAPJwtPayload = Depends(validate_iap_jwt)):
    if not q:
        return []
    users = search_services.search_users(q, limit)
    return users