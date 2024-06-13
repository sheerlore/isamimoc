from typing import List

from daos.user import UserDAO
from schemas.user import User

users_dao = UserDAO()

class UserService:
    def get_all_user(self) -> List[User]:
        return users_dao.getAll()