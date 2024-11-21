import streamlit as st
from auth import login_form, signup_form

# Configure Streamlit
st.set_page_config(page_title="Pencil Sketch Transformer", layout="centered")

# Session state for login tracking
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# Signup/Login Logic
if not st.session_state["logged_in"]:
    st.title("Welcome to Pencil Sketch Transformer! 🎨")
    st.markdown("Please log in or sign up to access the app.")

    tab1, tab2 = st.tabs(["Login", "Signup"])
    with tab1:
        login_form()
    with tab2:
        signup_form()

else:
    # Main App
    st.title(f"Welcome, {st.session_state['username']}!")
    st.markdown("Convert your photos into stunning pencil sketches! ✏️")

    # Logout button
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.rerun()

    # Sidebar options
    st.sidebar.header("Customize Sketch")
    blur_intensity = st.sidebar.slider("Blur Intensity", min_value=1, max_value=51, value=21, step=2)
    detail_level = st.sidebar.slider("Sketch Detail Level", min_value=50, max_value=300, value=256)

    # File upload and sketch functionality
    uploaded_file = st.file_uploader("📂 Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        from utils import create_pencil_sketch
        import numpy as np
        from PIL import Image

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