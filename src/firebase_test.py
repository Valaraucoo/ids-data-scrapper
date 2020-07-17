import pyrebase
from settings import *


config = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": FIREBASE_AUTH_DOMAIN,
    "databaseURL": FIREBASE_DATABASE_URL,
    "projectId": FIREBASE_PROJECT_ID,
    "storageBucket": FIREBASE_STORAGE_BUCKET,
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

data = {"Name": "John"}

db.child("bus-data").push(data)