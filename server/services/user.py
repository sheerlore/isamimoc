from typing import List

from daos.user import UserDAO
from schemas.user import UserFull, TmpStatus, SeatPos, IsAFK
from functools import lru_cache

users_dao = UserDAO()

class UserService:
    def get_all_user(self) -> List[UserFull]:
        return users_dao.get_all_user()
    
    def update_self_is_afk(self, email: str, data: IsAFK):
        return users_dao.set_my_is_afk(email, data)

    def update_self_tmp_status(self, email: str, data: TmpStatus):
        return users_dao.set_my_tmp_status(email, data)

    def update_self_seat_pos(self, email: str, data: SeatPos):
        return users_dao.set_my_seat_pos(email, data)
    
    @lru_cache
    def check_has_user_or_create(self, name: str, email: str):
        has_user = users_dao.check_user_in_DB(email)
        if has_user:
            return 
        users_dao.create_user(name, email) 
    
    @lru_cache
    def split_email(self, email: str):
        if "@" not in email:
            return email
        return email.split("@")
        
           