from typing import List

from database import db
from schemas.user import UserFull, TmpStatus, SeatPos, IsAFK

class UserDAO:
    def get_all_user(self) -> List[UserFull]:
        users_ref = db.collection("users")
        return [
            doc.to_dict()
            for doc in users_ref.get()
        ]
    
    def check_user_in_DB(self, email: str):
        query = db.collection("users").where("email", "==", email).stream()
        for doc in query:
            return bool(doc.to_dict())
            
            
    def create_user(self, name: str, email: str) -> UserFull:
        print("CREATE USER", name, email)
        user_ref = db.collection("users")
        doc_id = user_ref.document().id
        user_ref.document(doc_id).set({
            "name": name,
            "email": email,
            "is_afk": False,
            "tmp_status": {
                "icon": "",
                "comment": ""
            },
            "seat_pos": {
                "map_Id": 0,
                "x": 0,
                "y": 0
            }
        })
    
    # IS_AFK
    def set_my_is_afk(self, email: str, data: IsAFK):
        query = db.collection("users").where("email", "==", email).stream()
        for doc in query:
            user_dict = doc.to_dict()
            user_dict['is_afk'] = data.is_afk
            db.collection("users").document(doc.id).update(user_dict)
            return doc.to_dict()
    
    # TEMP STATUS
    def set_my_tmp_status(self, email: str, data: TmpStatus):
        query = db.collection("users").where("email", "==", email).stream()
        for doc in query:
            user_dict = doc.to_dict()
            user_dict['tmp_status']['icon'] = data.icon
            user_dict['tmp_status']['comment'] = data.comment
            db.collection("users").document(doc.id).update(user_dict)
            return doc.to_dict()

    # SEAT POS
    def set_my_seat_pos(self, email: str, data: SeatPos):
        query = db.collection("users").where("email", "==", email).stream()
        for doc in query:
            user_dict = doc.to_dict()
            user_dict['seat_pos']['map_Id'] = data.map_Id
            user_dict['seat_pos']['x'] = data.x
            user_dict['seat_pos']['y'] = data.y
            db.collection("users").document(doc.id).update(user_dict)
            return doc.to_dict()
        pass
    
