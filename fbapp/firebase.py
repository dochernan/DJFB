# fbapp/firebase.py

import firebase_admin
from firebase_admin import credentials, db
import os

# Path to the serviceAccountKey.json file
current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory, 'gothic-context-831-firebase-adminsdk-fbsvc-5c2fe4b90f.json')

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://gothic-context-831-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Replace with your Firebase database URL
})

# Reference to the Realtime Database
database_ref = db.reference()

# Function to add a user to Firebase
def add_user_to_firebase(name, email, gender, grade_level):
    user_ref = database_ref.child('users').push({
        'name': name,
        'email': email,
        'gender': gender,
        'grade_level': grade_level
    })
    return user_ref

#Function to retrieve all users from Firebase
def get_users_from_firebase():
    users_ref = database_ref.child('users')
    users = users_ref.get()  # Fetch all users from the database
    return users



