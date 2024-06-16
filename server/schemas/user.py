from typing import List
from pydantic import BaseModel

# Firestoreで用いるデータ基本的にドキュメント以下のデータを記述する

class User(BaseModel):
    name: str
    email: str
    is_afk: bool = False 

class TmpStatus(BaseModel):
    icon: str | None = None
    comment: str | None = None

class SeatPos(BaseModel):
    mapID: str
    x: int
    y: int

class SearchUser(BaseModel):
    token: List[str] 

class SearchResult(BaseModel):
    users: List[User]