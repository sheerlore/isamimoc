from mockfirestore import MockFirestore

db = MockFirestore()

userRef = db.collection('users')
userRef.add({
    "name": "satou.shouhei",
    "email": "satou.shouhei@gmail.com",
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

userRef.add({
    "name": "suzuki.shouta",
    "email": "suzuki.shouta@gmail.com",
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