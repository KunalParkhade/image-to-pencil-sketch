from firebase_config import db
import streamlit as st

USERS_COLLECTION = "users"

def signup_user(username, password):
    # Check if user already exists
    users_ref = db.collection(USERS_COLLECTION)
    if users_ref.document(username).get().exists:
        return False, "Username already exists."

    # Add new user to Firestore
    users_ref.document(username).set({"password": password})
    return True, "Signup successful!"

def login_user(username, password):
    # Verify credentials
    users_ref = db.collection(USERS_COLLECTION)
    user = users_ref.document(username).get()
    if user.exists:
        if user.to_dict().get("password") == password:
            return True, "Login successful!"
        return False, "Incorrect password."
    return False, "User does not exist."