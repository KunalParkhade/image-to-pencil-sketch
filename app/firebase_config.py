import streamlit as st
from firebase_admin import credentials, initialize_app, firestore

# Access Streamlit secrets
firebase_credentials = st.secrets["firebase_credentials"]

# Pass the dictionary directly to Certificate
cred = credentials.Certificate(dict(firebase_credentials))

# Initialize Firebase
initialize_app(cred)

# You can now use Firestore or other Firebase services
db = firestore.client()