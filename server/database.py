from mockfirestore import MockFirestore

db = MockFirestore()

userRef = db.collection('users')
userRef.add({
    'username': "name1",
    'email': "example1.com"
})
userRef.add({
    'username': "name2",
    'email': "example2.com"
})
