from firebase_config import db
import streamlit as st

USERS_COLLECTION = "users"

def signup_user(username, password):
    # check if user already exists
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


# import json
# import streamlit as st
# from pathlib import Path
# from hashlib import sha256


# def hash_password(password):
#     # """Hash the password using SHA-256 for security."""
#     # return sha256(password.encode()).hexdigest()
#     return hashlib.sha256(password.encode()).hexdigest()

# # Function to signup a new user
# def signup(username, password):
#     ref = db.reference("users")
#     users = ref.get() or {}

#     if username in users:
#         return False, "Username already exists!"
    
#     users[username] = {"password": hash_password(password)}
#     ref.set(users)
#     return True, "Signup successful!"


# # Function to login an existing user
# def login(username, password):
#     ref = db.reference("uses")
#     users = ref.get() or {}

#     if username not in users:
#         return False, "User not found!"
    
#     if users[username]["password"] != hash_password(password):
#         return False, "Incorrect password!"
    
#     return True, "Login successful!"


# # For local data storage below

# # # File path for user credentials
# # USER_DB_PATH = Path("app/users.json")

# # # Ensure the user database exists
# # if not USER_DB_PATH.exists():
# #     USER_DB_PATH.write_text(json.dumps({}))

# # def hash_password(password):
# #     # """Hash the password using SHA-256 for security."""
# #     # return sha256(password.encode()).hexdigest()

# # def save_user(username, password):
# #     """Save a new user to the database."""
# #     with USER_DB_PATH.open("r+") as file:
# #         users = json.load(file)
# #         if username in users:
# #             return False    # User already exists
# #         users[username] = hash_password(password)
# #         file.seek(0)
# #         json.dump(users, file)
# #         file.truncate()
# #     return True


# # def authenticate_user(username, password):
# #     """Authenticate an existing user."""
# #     with USER_DB_PATH.open("r") as file:
# #         users = json.load(file)
# #         if username in users and users[username] == hash_password(password):
# #             return True
# #     return False


# # def login_form():
# #     """Display the login form."""
# #     st.subheader("🔑 Login")
# #     username = st.text_input("Username")
# #     password = st.text_input("Password", type="password")
# #     if st.button("Login"):
# #         if authenticate_user(username, password):
# #             st.session_state["logged_in"] = True
# #             st.session_state["username"] = username
# #             st.success(f"Welcome back, {username}!")
# #             st.rerun()
# #         else:
# #             st.error("Invalid username or password!")

        

# # def signup_form():
# #     """Display the signup form."""
# #     st.subheader("📝 Signup")
# #     username = st.text_input("Create Username")
# #     password = st.text_input("Create Password", type="password")

# #     if st.button("Signup"):
# #         if save_user(username, password):
# #             st.success("Signup successful! Please log in.")
# #             st.rerun()
# #         else:
# #             st.error("Username already exists! Please try a different one.")