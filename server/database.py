from mockfirestore import MockFirestore

db = MockFirestore()

userRef = db.collection('users')
userRef.add({
    'name': "name1",
    'email': "example1.com",
    'is_afk': False
})
userRef.add({
    'name': "name2",
    'email': "example2.com",
    'is_afk': False
})
