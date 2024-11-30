import streamlit as st
from auth import signup_user, login_user
from utils import create_pencil_sketch
from PIL import Image
import numpy as np
import re

# Configure Streamlit
st.set_page_config(page_title="Pencil Sketch Transformer", layout="centered")

# Session state for login tracking
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# Validation functions
def validate_username(username):
    """Ensure username is alphanumeric and 3-15 characters long."""
    if not re.match(r"^[a-zA-Z0-9_]{3,15}$", username):
        return False, "Username must be 3-15 characters long and contain only letters, numbers, and underscores."
    return True, ""

def validate_password(password):
    """Ensure password has at least 8 characters, one number, one uppercase letter, and one special character."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, ""


# Signup/Login Logic
if not st.session_state["logged_in"]:
    st.title("Welcome to Pencil Sketch Transformer! 🎨")
    st.markdown("Log in or sign up to access the app.")

    # Create two columns for Login and Signup
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Login")
        username_login = st.text_input("Username (Login)", key="login_username")
        password_login = st.text_input("Password (Login)", type="password", key="login_password")
        if st.button("Login"):
            success, message = login_user(username_login, password_login)
            if success:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username_login
                st.success("Login successful!")
            else:
                st.error(message)

    with col2:
        st.subheader("Signup")
        username_signup = st.text_input("Username (Signup)", key="signup_username")
        password_signup = st.text_input("Password (Signup)", type="password", key="signup_password")

        if st.button("Signup"):
            # Validate username
            valid_username, username_message = validate_username(username_signup)
            if not valid_username:
                st.error(username_message)
            else:
                # Validate password
                valid_password, password_message = validate_password(password_signup)
                if not valid_password:
                    st.error(password_message)
                else:
                    # Proceed with signup
                    success, message = signup_user(username_signup, password_signup)
                    st.success(message) if success else st.error(message)
else:
    # Main App
    st.title(f"Welcome, {st.session_state['username']}!")
    st.markdown("Convert your photos into stunning pencil sketches! ✏️")

    # Logout button
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.experimental_rerun()

    # Sidebar options
    st.sidebar.header("Customize Sketch")
    blur_intensity = st.sidebar.slider("Blur Intensity", min_value=1, max_value=51, value=21, step=2)
    detail_level = st.sidebar.slider("Sketch Detail Level", min_value=50, max_value=300, value=256)

    # File upload and sketch functionality
    uploaded_file = st.file_uploader("📂 Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Convert the uploaded file to an image
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        # Display the original image
        st.subheader("Original Image")
        st.image(image, caption="Original Image", use_container_width=True)

        # Create the pencil sketch
        pencil_sketch = create_pencil_sketch(image_np, blur_intensity, detail_level)

        # Display the pencil sketch
        st.subheader("Pencil Sketch")
        st.image(pencil_sketch, caption="Pencil Sketch", use_container_width=True, clamp=True, channels="GRAY")

        # Convert sketch back to PIL format in RGB mode for downloading
        sketch_pil = Image.fromarray(pencil_sketch).convert("RGB")

        # Provide download option
        st.download_button(
            label="Download Sketch",
            data=sketch_pil.tobytes("jpeg", "RGB"),
            file_name="pencil_sketch.jpg",
            mime="image/jpeg",
        )