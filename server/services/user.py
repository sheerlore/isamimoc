from typing import List

from daos.user import UserDAO
from schemas.user import User
from functools import lru_cache

users_dao = UserDAO()

class UserService:
    def get_all_user(self) -> List[User]:
        return users_dao.get_all_user()

    def get_all_doc(self):
        return users_dao.get_all_user_doc_id()
    
    @lru_cache
    def check_has_user_or_create(self, name: str, email):
        has_user = users_dao.check_user_in_DB(email)
        if has_user:
            print("USER_HAS:", has_user)
            return 
        users_dao.create_user(name, email) 
    
    def split_email(self, email: str):
        if "@" not in email:
            return email
        return email.split("@")
        
           