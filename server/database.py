from mockfirestore import MockFirestore

db = MockFirestore()

userRef = db.collection('users')
