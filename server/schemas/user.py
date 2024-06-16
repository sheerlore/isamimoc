from typing import TypeAlias
from pydantic import BaseModel, ConfigDict


Email: TypeAlias = str

# Firestoreのデータ構造で用いるデータ

class IsAFK(BaseModel):
    """
    離席中かどうか
    例：
    {
        "is_afk": False
    }
    """
    is_afk: bool

class TmpStatus(BaseModel):
    """
    一時ステータス
    例：
    {
        "icon": "😁",
        "comment": "smile"
    }
    """
    icon: str
    comment: str

class SeatPos(BaseModel):
    """
    マップ情報
    例：
    {
        "map_Id": 0,
        "x": 30,
        "y": 20,
    }
    """
    map_Id: int 
    x: int
    y: int

class User(IsAFK):
    """
    ユーザー基本情報
    例：
    {
        "name": mail.example,
        "email": mail.example.com,
        "is_afk": False,
    }
    """
    name: str
    email: str

class UserFull(User):
    """
    ユーザー完全情報
    例：
    {
        "name": mail.example,
        "email": mail.example.com,
        "is_afk": False,
        "tmp_status": {
            "icon": "😁",
            "comment": "smile"
        },
        "seat_pos": {
            "map_Id": 0,
            "x": 30,
            "y": 20,
        },
        
    }
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
    tmp_status: TmpStatus
    seat_pos: SeatPos