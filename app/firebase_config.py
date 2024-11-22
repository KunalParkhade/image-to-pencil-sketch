import firebase_admin
from firebase_admin import credentials, firestore

# Path to your Firebase credentials
CREDENTIALS_PATH = "firebase_credentials.json"

# Initialize Firebase app
cred = credentials.Certificate(CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)

# Initialize firestore
db = firestore.client()