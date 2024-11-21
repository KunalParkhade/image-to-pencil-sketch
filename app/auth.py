import json
import streamlit as st
from pathlib import Path
from hashlib import sha256

# File path for user credentials
USER_DB_PATH = Path("app/users.json")

# Ensure the user database exists
if not USER_DB_PATH.exists():
    USER_DB_PATH.write_text(json.dumps({}))


def hash_password(password):
    """Hash the password using SHA-256 for security."""
    return sha256(password.encode()).hexdigest()


def save_user(username, password):
    """Save a new user to the database."""
    with USER_DB_PATH.open("r+") as file:
        users = json.load(file)
        if username in users:
            return False    # User already exists
        users[username] = hash_password(password)
        file.seek(0)
        json.dump(users, file)
        file.truncate()
    return True


def authenticate_user(username, password):
    """Authenticate an existing user."""
    with USER_DB_PATH.open("r") as file:
        users = json.load(file)
        if username in users and users[username] == hash_password(password):
            return True
    return False


def login_form():
    """Display the login form."""
    st.subheader("🔑 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Welcome back, {username}!")
            st.rerun()
        else:
            st.error("Invalid username or password!")

        

def signup_form():
    """Display the signup form."""
    st.subheader("📝 Signup")
    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")

    if st.button("Signup"):
        if save_user(username, password):
            st.success("Signup successful! Please log in.")
            st.rerun()
        else:
            st.error("Username already exists! Please try a different one.")