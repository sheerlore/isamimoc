from typing import List

from database import db
from schemas.user import User 

class UserDAO:
    collection_name = "users"

    def getAll(self) -> List[User]:
        users_ref = db.collection(self.collection_name)
        return [
            User(**doc.get().to_dict())
            for doc in users_ref.list_documents()
            if doc.get().to_dict()
        ]