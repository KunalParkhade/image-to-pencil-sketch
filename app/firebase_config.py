import json
import streamlit as st
from firebase_admin import credentials, initialize_app

# Load Firebase credentials from Streamlit secrets
firebase_credentials = st.secrets["firebase_credentials"]

# Convert the credentials to a format Firebase understands
cred = credentials.Certificate(firebase_credentials)

# Initialize Firebase app
initialize_app(cred)

# You can now use Firestore or other Firebase services