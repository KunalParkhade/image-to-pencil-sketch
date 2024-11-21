import streamlit as st
import numpy as np
from PIL import Image
from utils import create_pencil_sketch
import cv2

# Streamlit app title and description
st.set_page_config(page_title="Pencil Sketch Transformer", layout="centered")
st.title("🎨 Pencil Sketch Transformer")
st.markdown("Convert your photos into stunning pencil sketches in seconds! ✏️")

st.sidebar.header("Customize Sketch")
blur_intensity = st.sidebar.slider("Blur Intensity", min_value=1, max_value=51, value=21, step=2)
detail_level = st.sidebar.slider("Sketch Detail Level", min_value=50, max_value=300, value=256)

# Upload image
uploaded_file = st.file_uploader("📂 Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Convert uploaded file to image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Display original image
    st.subheader("Original Image")
    st.image(image, caption="Original Image", use_container_width=True)

    # create a pencil sketch
    pencil_sketch = create_pencil_sketch(image_np, blur_intensity, detail_level)

    # Display pencil sketch
    st.subheader("Pencil sketch")
    st.image(pencil_sketch,caption="Pencil Sketch", use_container_width=True, clamp=True, channels="GRAY")

    # Sketch back to PIL for downloading
    sketch_pil = Image.fromarray(pencil_sketch).convert("RGB")

    # Provide download option
    st.download_button(
        label="Download Sketch",
        data=sketch_pil.tobytes("jpeg", "RGB"),
        file_name="pencil_sketch.jpg",
        mime="image/jpeg",
    )

# Footer styling
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
        footer {visibility: hidden;}
        .reportview-container {background: #f4f4f9;}
        header {visibility: hidden;}
    </style>
    <footer>Powered by Streamlit | Made with 💖 by Kunal Parkhade</footer>
    """,
    unsafe_allow_html=True
)