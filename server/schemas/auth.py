from pydantic import BaseModel

# Google Cloud Identity Aware Proxy (IAP)でHeaaerに格納されるJWTトークンをデコードした結果に得られるデータ
# sub: ユーザーごとに一意なので、user_idとして扱える
# email: メールアドレス
class IAPJwtPayload(BaseModel):
    sub: str
    email: str
    

