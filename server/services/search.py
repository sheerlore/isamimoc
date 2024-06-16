
from daos.user import UserDAO
# from schemas.user import UserFull

users_dao = UserDAO()

class SearchService:
    def search_users(q: str, limit: int):
        return users_dao.search_users_by_query(q, limit)