from typing import List

from database import db
from schemas.user import User, TmpStatus, SeatPos

class UserDAO:
    collection_name = "users"

    def get_all_user(self) -> List[User]:
        users_ref = db.collection(self.collection_name)
        return [
            User(**doc.get().to_dict())
            for doc in users_ref.list_documents()
            if doc.get().to_dict()
        ]
    
    def get_all_user_doc_id(self):
        user_doc_ref= db.collection(self.collection_name)
        return [
            doc.id
            for doc in user_doc_ref.get()
        ]
    
    def check_user_in_DB(self, email: str):
        query = db.collection(self.collection_name).where("email", "==", email).stream()
        for doc in query:
            return bool(doc.to_dict())
            
            
    def create_user(self, name: str, email: str) -> User:
        print("CREATE USER", name, email)
        db.collection(self.collection_name).add({
            "name": name,
            "email": email,
            "is_afk": False
        })

class UserTmpStatusDAO:
    collection_name = "tmp-status"
    
    def set_my_icon(self, icon: str):
        pass

    def set_my_comment(self, comment: str):
        pass

class UserSeatPosDAO:
    collection_name = "seat-pos"

    def set_my_map_id(self, map_id: str):
        pass
    
    def set_my_pos(self, x: int, y: int):
        pass